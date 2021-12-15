from django.db.models import Model, CharField, BooleanField, ManyToManyField

class Substance(Model):
    name = CharField(max_lenght=20)
    is_active = BooleanField(default=True)
    do_not_use_with = ManyToManyField("self", related_name="forbidden")


