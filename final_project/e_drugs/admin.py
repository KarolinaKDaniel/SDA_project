from django.contrib import admin

from .models import Alert, Shipping


# Register your models here.
admin.site.register(Alert)
admin.site.register(Shipping)