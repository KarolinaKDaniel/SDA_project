from django.contrib import admin

from .models import MyUser, Doctor, Patient, Pharmacist

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Pharmacist)
