from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from toys.models import Toy

@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your models here.
class Customer(AbstractUser):
    address = models.TextField(default="")
    contact_number = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "{} | {} {}".format(self.username, self.first_name, self.last_name)


class HoppList(models.Model):
    toys = models.ManyToManyField(Toy)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "[id: {}] {} items for {}".format(self.id, self.toys.count(), self.customer.username)


class Subscription(models.Model):
    hopplist = models.ForeignKey(HoppList, on_delete=models.SET_NULL, null=True)
    # hopplist

    address = models.TextField(default="")
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "Subscription #{} of {} items for {}".format(self.id, self.hopplist.toys.count(), self.customer.username)

    @property
    def customer(self):
        return self.hopplist.customer
