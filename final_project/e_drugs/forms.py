from django.forms import ModelForm, IntegerField
from django.forms.widgets import NumberInput
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

    quantity = IntegerField(widget=NumberInput, min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
