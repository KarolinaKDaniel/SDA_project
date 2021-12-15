from django.db import models
from django.db.models import Model, CharField, TextField, FloatField


class Alert(Model):
    name = CharField(max_length=128)
    recommendations = TextField()


class Shipping(Model):
    name = CharField(max_length=128)
    price = FloatField()


# Create your models here.
