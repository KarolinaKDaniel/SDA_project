from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, Model, CASCADE, ImageField, OneToOneField, ManyToManyField
from e_drugs.models import Affliction


class MyUser(User):
    address = CharField(max_length=256)
    phone = CharField(max_length=20)
    Personal_ID = CharField(max_length=20)


class Doctor(Model):
    my_user = OneToOneField(MyUser, on_delete=CASCADE)
    specialization = CharField(max_length=128)
    credential_id = CharField(max_length=128)
    photo = ImageField(blank=True, null=True)


class Patient(Model):
    doctor = ManyToManyField(Doctor, blank=True)
    my_user = OneToOneField(MyUser, on_delete=CASCADE)
    affliction = ManyToManyField(Affliction, blank=True)


class Pharmacist(Model):
    my_user = OneToOneField(MyUser, on_delete=CASCADE)
    credential_id = CharField(max_length=128)
