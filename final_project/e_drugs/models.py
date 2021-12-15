from django.db import models
from django.db.models import Model, CharField, TextField


class Alert(Model):
    name = CharField(max_length=128)
    recommendations = TextField()

# Create your models here.
