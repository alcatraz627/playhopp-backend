import os
from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.core.files.storage import FileSystemStorage
from rest_framework.authtoken.models import Token
from toys.models import Toy

# For uploading images
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

def nameCustomerDP(instance, filename):
    return '/'.join(['customer', '.'.join([str(instance.id), filename.split('.')[-1]]) ])

# Create auth token when a user is registered/logged in
@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create a hopplist automatically when a user is created
@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_hopplist(sender, instance=None, created=False, **kwargs):
    if created:
        HoppList.objects.get_or_create(customer=instance, current=True)


# TODO: Hopplist archive and recreate new
# TODO: Subscription create when hopplist

# Create your models here.
class Customer(AbstractUser):
    address = models.TextField(default="")
    contact_number = models.CharField(max_length=20)

    profile_pic = models.ImageField(upload_to=nameCustomerDP, storage=fs, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        # return "e"
        return "{} | {} {}".format(self.username, self.first_name, self.last_name)


class HoppList(models.Model):
    toys = models.ManyToManyField(Toy)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    current = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # TODO: Renew

    def __str__(self):
        # return "e"
        return "[id: {}] {} items for {}".format(self.id, self.toys.count(), self.customer.username)

# https://hackernoon.com/using-enum-as-model-field-choice-in-django-92d8b97aaa63
class SubscPlanEnum(Enum):
    ONE = 'ONE'
    THREE = 'THREE'
    SIX = 'SIX'

class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    address = models.TextField(default="")
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    plan = models.CharField(max_length=20, choices=[(plan, plan.value) for plan in SubscPlanEnum], default=SubscPlanEnum.ONE)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # TODO: Figure
    # paid = models.BooleanField(default=False)
    # start_date
    # duration


    def __str__(self):
        return "Subscription [Hopplist: #{}] of {} items for {}".format(self.id, self.hopplist.toys.count(), self.customer.username)

    @property
    def hopplist(self):
        return HoppList.objects.get_or_create(customer=self.customer, current=True)[0]


class ForgotPass(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    verif_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.customer.username} | {self.verif_code}"