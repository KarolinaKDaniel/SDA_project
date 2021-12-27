import json

from django.forms import ModelForm, CharField, DecimalField, JSONField, ModelChoiceField, HiddenInput, Widget, \
    IntegerField, ChoiceField
from django.template.loader import render_to_string

from .models import Medicine, Substance


#
# class SubstanceAndDoseWidget(Widget):
#
#     def __init__(self, *args, **kwargs):
#         self.substance_name = ModelChoiceField(queryset=Substance.objects.all())
#         self.substance_dose = IntegerField()

class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'substance': HiddenInput(),
            'refundation': DecimalField(max_value=100, min_value=0, initial=100),
            'form': ChoiceField(choices=Medicine.CHOICES),
            'price_net': DecimalField()
        }
