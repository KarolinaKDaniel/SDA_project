import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, DecimalField, BooleanField, JSONField, Textarea

from .models import Medicine

class MedicineForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = Medicine

    name = CharField(max_length=128, label='Market name')
    refundation = DecimalField(min_value=0, max_value=100,
                               initial=100, decimal_places=2,
                               label='Percent of price after refundation')
    price_net = DecimalField(min_value=0, decimal_places=2)
    need_prescription = BooleanField(label='Check if the medicine needs prescription')
    doses = JSONField(widget=Textarea,
                      label='Fill in with name of substance and dose in ml accordingly eg.: { "substance": "60" }',
                      initial={})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
