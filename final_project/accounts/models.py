from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, Model, CASCADE, ImageField, OneToOneField


class MyUser(User):
    address = CharField(max_length=256)
    phone = CharField(max_length=20)
    Personal_ID = CharField(max_length=20)

    class Meta:
        verbose_name = "MyUser"

class Doctor(MyUser):
    specialization = CharField(max_length=128)
    credential_id = CharField(max_length=128)
    photo = ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "Doctor"

class Pharmacist(MyUser):
    credential_id = CharField(max_length=128)

    class Meta:
        verbose_name = "Pharmacist"