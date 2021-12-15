from django.contrib import admin

from .models import Discount, Alert, Shipping, Substance, Affliction, Medicine


# Register your models here.
admin.site.register(Alert)
admin.site.register(Discount)
admin.site.register(Shipping)
admin.site.register(Substance)
admin.site.register(Medicine)
admin.site.register(Affliction)
