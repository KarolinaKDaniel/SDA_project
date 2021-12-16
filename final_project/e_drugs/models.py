from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, ManyToManyField, FloatField, ImageField, \
    JSONField


class Alert(Model):
    name = CharField(max_length=128)
    recommendations = TextField()


class Discount(Model):
    name = CharField(max_length=128)
    amount = FloatField()
    aplied_when_over = FloatField()


class Shipping(Model):
    name = CharField(max_length=128)
    price = FloatField()


# Create your models here.
class Substance(Model):
    name = CharField(max_length=20)
    is_active = BooleanField(default=True)
    do_not_use_with = ManyToManyField("Substance", related_name="forbidden")


class Affliction(Model):
    name = CharField(max_length=128)
    do_not_use = ManyToManyField(Substance, related_name="forbidden_sub")


class Medicine(Model):
    name = CharField(max_length=128)
    substance = ManyToManyField(Substance)
    doses = JSONField()
    refundation = FloatField()
    need_prescription = BooleanField()
    form = CharField(max_length=128)
    alerts = ManyToManyField(Alert)
    manufacturer = CharField(max_length=128)
    price_net = FloatField()
    image = ImageField(blank=True, null=True)
