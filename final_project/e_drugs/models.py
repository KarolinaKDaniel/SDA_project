from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, ManyToManyField, IntegerField, FloatField


class Alert(Model):
    name = CharField(max_length=128)
    recommendations = TextField()


class Discount(Model):
    name = CharField(max_length=128)
    amount = IntegerField()


class Shipping(Model):
    name = CharField(max_length=128)
    price = FloatField()


# Create your models here.
class Substance(Model):
    name = CharField(max_length=20)
    is_active = BooleanField(default=True)
    do_not_use_with = ManyToManyField("Substance", related_name="forbidden")
