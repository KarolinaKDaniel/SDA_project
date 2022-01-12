from django.forms import ModelForm, MultipleHiddenInput, MultipleChoiceField, NumberInput, TextInput, ModelChoiceField, \
    Select, DecimalField, ModelMultipleChoiceField, IntegerField
from .form_utils import CustomDoseField, CustomDoseWidget

from django.forms import ModelForm
from django.template.loader import render_to_string

from .models import Medicine, Prescription, SideEffect, Substance


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'substance': Select()
        }

    refundation = DecimalField(min_value=0, max_value=100, decimal_places=2)
    price_net = DecimalField(min_value=0, decimal_places=2)
    doses = IntegerField(widget=NumberInput, min_value=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        pass


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