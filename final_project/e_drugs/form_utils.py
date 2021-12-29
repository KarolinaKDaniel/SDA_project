from django.core.exceptions import ValidationError
from django.forms import MultiWidget, Select, NumberInput, MultiValueField, ChoiceField, IntegerField
from .models import Substance


class CustomDoseWidget(MultiWidget):
    def __init__(self, *args, **kwargs):
        substances = [subs.name for subs in Substance.objects.all()]
        widgets = [
            Select(choices=substances),
            NumberInput()
        ]
        super().__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if isinstance(value, dict):
            for key in value.keys():
                return [key, value[key]]
        elif isinstance(value, str):
            decompressed_value = value.strip('{} "')
            decompressed_value = decompressed_value.split(":")
            return decompressed_value
        return [None, None]


class CustomDoseField(MultiValueField):
    def __init__(self, *args, **kwargs):
        choices = list(Substance.objects.all())
        error_messages = {
            'incomplete': 'Choose a substance and put in the dose ammount in ml'
        }
        fields = {
            ChoiceField(choices=choices),
            IntegerField(min_value=0)
        }
        # widget = CustomDoseWidget
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in self.empty_values or data_list[1] in self.empty_values:
                raise ValidationError(self.error_messages['incomplete'])
            result = '{' + f' "{data_list[0].name}": "{data_list[1]}" ' + '}'