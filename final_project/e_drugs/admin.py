from django.contrib import admin

from .models import Alert, Shipping, Substance, Discount


# Register your models here.
admin.site.register(Alert)
admin.site.register(Discount)
admin.site.register(Shipping)
admin.site.register(Substance)
