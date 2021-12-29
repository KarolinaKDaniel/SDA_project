from django.db.models import Model, CharField, TextField, BooleanField, ManyToManyField, FloatField, ForeignKey, \
    DateField, DO_NOTHING, JSONField, ImageField, DateTimeField, IntegerField
from .form_utils import CustomDoseField


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
    do_not_use_with = ManyToManyField("Substance", blank=True, symmetrical=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name



class Affliction(Model):
    name = CharField(max_length=128)
    do_not_use = ManyToManyField(Substance, related_name="forbidden_sub", blank=True)

    def __str__(self):
        return self.name


class Medicine(Model):
    CHOICES = [
        ('pill', 'pill'),
        ('capsule', 'capsule'),
        ('cream', 'cream'),
        ('powder', 'powder'),
        ('spray', 'spray'),
        ('syrup', 'syrup'),
        ('dragee', 'dragee'),
        ('suppository', 'suppository'),
        ('ointment', 'ointment'),
        ('gel', 'gel'),
        ('emulsion', 'emulsion'),
        ('suspension', 'suspension'),
        ('solution', 'solution')
    ]
    name = CharField(max_length=128)
    substance = ManyToManyField(Substance)
    doses = CustomDoseField(choices=Substance.objects.all())
    refundation = FloatField()
    need_prescription = BooleanField()
    form = CharField(choices=CHOICES, max_length=15)
    alerts = ManyToManyField(Alert, blank=True)
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
        ('accepted', 'accepted'),
        ('paid', 'paid'),
        ('processed', 'processed'),
        ('shipped', 'shipped'),
    )
    patient = ForeignKey('accounts.Patient', on_delete=DO_NOTHING)
    medicine_instance = ManyToManyField(MedicineInstance)
    created = DateTimeField(auto_now_add=True)
    state = CharField(max_length=9, choices=CHOICES)
    shipping = ForeignKey(Shipping, on_delete=DO_NOTHING)
    discount = ForeignKey(Discount, on_delete=DO_NOTHING, null=True, blank=True)


class Prescription(Model):
    VALID_CHOICES = (
        (120, "foreign"),
        (30, "standard"),
        (7, "antibiotic")
    )

    prescribed_by = ForeignKey('accounts.MyUser', on_delete=DO_NOTHING)
    patient = ForeignKey('accounts.Patient', on_delete=DO_NOTHING)
    medicine = ManyToManyField(Medicine, related_name="medicine")
    created = DateTimeField(auto_now_add=True)
    valid = IntegerField(choices=VALID_CHOICES, default="standard")
    is_used = BooleanField(default=False)
    comment = TextField()

    def __str__(self):
        return f'{self.patient.my_user.first_name} {self.patient.my_user.last_name}: {self.created}'

class SideEffect(Model):
    patient = ForeignKey('accounts.Patient', on_delete=DO_NOTHING)
    medicine = ForeignKey(Medicine, on_delete=DO_NOTHING)
    what_effect = TextField()


