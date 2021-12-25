import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, DecimalField, BooleanField, JSONField, Textarea, Select, Field, \
    ModelChoiceField, Form, IntegerField, MultiWidget, TextInput, NumberInput, Widget
from json_model_widget.widgets import JsonPairInputs

from .models import Medicine, Substance, Alert

class MedicineForm(ModelForm):

    class Meta:
        model = Medicine
        fields = '__all__'

    name = CharField(max_length=128)
    substance = ModelChoiceField(queryset=Substance.objects.all())
    doses = IntegerField()
    refundation = DecimalField(min_value=0, max_value=100, decimal_places=2, initial=100)
    need_prescription = BooleanField(initial=False)
    form = Select(Medicine.CHOICES)
    alerts = ModelChoiceField(queryset=Alert.objects.all(), required=False)
    manufacturer = CharField(max_length=128)
    price_net = DecimalField(decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_doses(self):
        cleaned_doses =

    # class Meta:
    #     model = Medicine
    #     fields = '__all__'
    #
    #     widgets = {
    #         'doses': CustomDosesWidget
    #     }
    #
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         for visible in self.visible_fields():
    #             visible.field.widget.attrs['class'] = 'form-control'
    #
    # def clean_doses(self):
    #     doses_cleaned =