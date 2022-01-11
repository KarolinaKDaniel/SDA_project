from django.forms import ModelForm, MultipleHiddenInput, MultipleChoiceField, NumberInput, TextInput, ModelChoiceField, \
    Select, DecimalField, ModelMultipleChoiceField, IntegerField
from .form_utils import CustomDoseField, CustomDoseWidget

from .models import Medicine, Substance


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
