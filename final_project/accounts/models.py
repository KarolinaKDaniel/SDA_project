from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextField, IntegerField, CharField

class MyUser(User):
    address = CharField(max_length=256)
    phone = CharField(max_length=20)
    Personal_ID = CharField(max_length=20)