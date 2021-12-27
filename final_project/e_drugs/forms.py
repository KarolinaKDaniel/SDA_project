import json

from django.core.exceptions import ValidationError
from django.forms import ModelForm, MultiWidget, Select, NumberInput, IntegerField, ChoiceField, MultipleHiddenInput, \
    MultiValueField, SplitDateTimeField

from .models import Medicine, Substance


class CustomDoseWidget(MultiWidget):
    def __init__(self, *args, **kwargs):
        substances = Substance.objects.all()
        widgets = [
            Select(choices=substances),
            NumberInput()
        ]
        super().__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if isinstance(value, Substance):
            return value.name
        elif isinstance(value, int):
            return value
        return [None, None]


class CustomDoseField(MultiValueField):
    def __init__(self, *args, **kwargs):
        choices = Substance.objects.all()
        error_messages = {
            'incomplete': 'Choose a substance and put in the dose ammount in ml'
        }
        fields = {
            ChoiceField(choices=choices),
            IntegerField(min_value=0)
        }
        widget = CustomDoseWidget
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in self.empty_values or data_list[1] in self.empty_values:
                raise ValidationError(self.error_messages['incomplete'])
            result = '{' + f' "{data_list[0].name}": "{data_list[1]}" ' + '}'

class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'substance': MultipleHiddenInput(),
        }

    doses = CustomDoseField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
