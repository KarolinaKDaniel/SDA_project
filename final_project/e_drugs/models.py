from django.db.models import Model, CharField, TextField, BooleanField, ManyToManyField, FloatField, ForeignKey, \
    DateField, DO_NOTHING, JSONField, ImageField, DateTimeField, IntegerField


class Alert(Model):
    name = CharField(max_length=128)
    recommendations = TextField()

    def __str__(self):
        return self.name


class Discount(Model):
    name = CharField(max_length=128)
    amount = FloatField()
    apply_when_over = FloatField()

    def __str__(self):
        return self.name


class Shipping(Model):
    name = CharField(max_length=128)
    price = FloatField()

    def __str__(self):
        return self.name


class Substance(Model):
    name = CharField(max_length=20)
    is_active = BooleanField(default=True)
    do_not_use_with = ManyToManyField("Substance", related_name="forbidden", blank=True)

    def __str__(self):
        return self.name


class Affliction(Model):
    name = CharField(max_length=128)
    do_not_use = ManyToManyField(Substance, related_name="forbidden_sub")

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class MedicineInstance(Model):
    medicine = ForeignKey(Medicine, on_delete=DO_NOTHING)
    expire_date = DateField()
    is_damaged = BooleanField(default=False)
    code = CharField(max_length=64)

    def __str__(self):
        return self.medicine.name


class Order(Model):
    CHOICES = (
        ('A', 'accepted'),
        ('P', 'paid'),
    )
    patient = ForeignKey('accounts.Patient', on_delete=DO_NOTHING)
    medicine_instance = ManyToManyField(MedicineInstance)
    created = DateTimeField(auto_now_add=True)
    state = CharField(max_length=1, choices=CHOICES)
    shipping = ForeignKey(Shipping, on_delete=DO_NOTHING)
    discount = ManyToManyField(Discount, null=True)


class Prescription(Model):
    VALID_CHOICES = (
        ("foreign", 120),
        ("standard", 30),
        ("antibiotic", 7)
    )

    prescribed_by = ForeignKey('accounts.MyUser', on_delete=DO_NOTHING)
    patient = ForeignKey('accounts.Patient', on_delete=DO_NOTHING)
    medicine = ManyToManyField(Medicine, related_name="medicine")
    created = DateTimeField(auto_now_add=True)
    valid = IntegerField(choices=VALID_CHOICES, default="standard")
    is_used = BooleanField(default=False)
    comment = TextField()


class SideEffect(Model):
    patient = ForeignKey('accounts.Patient', on_delete=DO_NOTHING)
    medicine = ForeignKey(Medicine, on_delete=DO_NOTHING)
    what_effect = TextField()
