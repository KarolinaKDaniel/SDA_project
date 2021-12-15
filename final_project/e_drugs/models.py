from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, ManyToManyField


class Alert(Model):
    name = CharField(max_length=128)
    recommendations = TextField()


# Create your models here.
class Substance(Model):
    name = CharField(max_length=20)
    is_active = BooleanField(default=True)
    do_not_use_with = ManyToManyField("self", related_name="forbidden")
