from django.contrib import admin

# Register your models here.
from .models import Customer, HoppList, Subscription, ForgotPass
admin.site.register(Customer)
admin.site.register(HoppList)
admin.site.register(Subscription)
admin.site.register(ForgotPass)
