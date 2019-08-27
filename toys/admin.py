from django.contrib import admin

# Register your models here.
from .models import Toy, Category, Brand

admin.site.register(Toy)
admin.site.register(Category)
admin.site.register(Brand)
