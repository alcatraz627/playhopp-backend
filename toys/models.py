from django.db import models
from django.conf import settings


# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=200)
    # logo

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    # image
    def __str__(self):
        return self.title


class Toy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    skills = models.TextField(default="")
    playIdeas = models.TextField(default="")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    # primaryImage = >img
    # images = >img
    primaryImage = models.CharField(default="", max_length=800)
    minAge = models.IntegerField()
    maxAge = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # @property
    # def likes(self):
    #     return 300

    def __str__(self):
        return self.title
