import os
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
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    current = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # TODO: Renew

    def __str__(self):
        # return "e"
        return "[id: {}] {} items for {}".format(self.id, self.toys.count(), self.customer.username)


class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    address = models.TextField(default="")
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # paid = models.BooleanField(default=False)
    # start_date
    # duration


    def __str__(self):
        # return "e"
        return "Subscription [Hopplist: #{}] of {} items for {}".format(self.id, self.hopplist.toys.count(), self.customer.username)

    @property
    def hopplist(self):
        return HoppList.objects.get_or_create(customer=self.customer, current=True)[0]
