from django.contrib import admin

from .models import Discount, Alert, Shipping, Substance, Affliction


# Register your models here.
admin.site.register(Alert)
admin.site.register(Discount)
admin.site.register(Shipping)
admin.site.register(Substance)

admin.site.register(Affliction)
