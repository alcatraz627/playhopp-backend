from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    address = models.TextField(default="")
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return "{} | {} {}".format(self.username,self.first_name, self.last_name)
