import json

from django.forms import ModelForm, CharField, DecimalField, JSONField, ModelChoiceField
from django.template.loader import render_to_string
from json_model_widget.widgets import JsonPairInputs

from .models import Medicine, Substance, Alert, Dose

class CustomJsonField(JsonPairInputs):

    def render(self, name, value, attrs=None, renderer=None) -> str:

        if value is None or value.strip() is '':
            value = '{}'

        context = {
            "col1": self.col1.all(),
            "col2": self.col2.all(),
            "json": json.loads(value),
            "name": name
        }

        return render_to_string('json_template.html', context=context)


class MedicineForm(ModelForm):

    class Meta:
        model = Medicine
        fields = '__all__'

    doses = JSONField(widget=CustomJsonField(Substance, Dose))
    refundation = DecimalField(min_value=0, max_value=100, decimal_places=2, initial=100)
    form = Select(Medicine.CHOICES)
    alerts = ModelChoiceField(queryset=Alert.objects.all(), required=False)
    manufacturer = CharField(max_length=128)
    price_net = DecimalField(decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

