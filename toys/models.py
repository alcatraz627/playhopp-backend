import os
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# For uploading images
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

def nameFile(mediaType):
    def f(instance, filename):
        return '/'.join([mediaType, '.'.join([str(instance.id), filename.split('.')[-1]]) ])

    return f

# MEDIA_ROOT/toys/{id}.jpg
# MEDIA_ROOT/toys/{id}_1.jpg
def nameToyImage(toyNumbering):
    def f(instance, filename):
        return '/'.join([toyNumbering, '.'.join([str(instance.id), filename.split('.')[-1]]) ])

    return f



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
    minAge = models.IntegerField(default=3)
    maxAge = models.IntegerField(default=8)
    piecesNumber = models.CharField(default="", max_length=100)
    points = models.IntegerField(default=1)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # @property
    # def likes(self):
    #     return 300

    def __str__(self):
        return "{} | {}".format(self.title, self.id)
