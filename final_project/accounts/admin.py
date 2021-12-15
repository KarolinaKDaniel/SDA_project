from django.contrib import admin

from .models import MyUser, Doctor

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Doctor)
