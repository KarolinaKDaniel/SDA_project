from django.contrib import admin

from .models import Discount, Alert, Shipping, Substance, Affliction, Medicine, MedicineInstance, Prescription

admin.site.register(Alert)
admin.site.register(Discount)
admin.site.register(Shipping)
admin.site.register(Substance)
admin.site.register(MedicineInstance)
admin.site.register(Medicine)
admin.site.register(Affliction)
admin.site.register(Prescription)
