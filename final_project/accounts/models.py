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

    class Meta:
        ordering = ['my_user__last_name']


class Patient(Model):
    doctor = ManyToManyField(Doctor)
    my_user = OneToOneField(MyUser, on_delete=CASCADE)
    affliction = ManyToManyField(Affliction)


class Pharmacist(Model):
    my_user = OneToOneField(MyUser, on_delete=CASCADE)
    credential_id = CharField(max_length=128)
