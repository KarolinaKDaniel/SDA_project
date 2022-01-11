import json

from django.forms import ModelForm, NumberInput
from django.db.models import IntegerField, CharField, DateField
from django.template.loader import render_to_string

from .models import Medicine, Prescription, SideEffect, MedicineInstance


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['is_used']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SideEffectForm(ModelForm):
    class Meta:
        model = SideEffect
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MedicineInstanceForm(ModelForm):
    class Meta:
        model = MedicineInstance
        fields = '__all__'
        widgets = {
            'quantity': NumberInput
        }
    # quantity = IntegerField()
    # medicine = CharField()
    # code = CharField()
    # expire_date = DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
