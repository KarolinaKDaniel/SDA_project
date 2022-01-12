from django.forms.widgets import NumberInput
from .models import Medicine, Prescription, SideEffect, MedicineInstance
from django.forms import ModelForm, NumberInput, Select, DecimalField, IntegerField

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
    dose = IntegerField(widget=NumberInput, min_value=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['is_used']
        widgets = {'prescribed_by': HiddenInput}

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

    quantity = IntegerField(widget=NumberInput, min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
