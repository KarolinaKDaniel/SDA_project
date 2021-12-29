from django.forms import ModelForm, MultipleHiddenInput, \
    MultipleChoiceField
from .form_utils import CustomDoseField, CustomDoseWidget

from .models import Medicine, Substance


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

    substance = MultipleChoiceField(widget=MultipleHiddenInput())
    doses = CustomDoseField(choices=Substance.objects.all(), widget=CustomDoseWidget(choices=Substance.objects.all()))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
