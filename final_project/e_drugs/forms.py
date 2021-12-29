from django.forms import ModelForm, MultipleHiddenInput, \
    MultipleChoiceField
from .form_utils import CustomDoseField, CustomDoseWidget

from .models import Medicine


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

    substance = MultipleChoiceField(widget=MultipleHiddenInput())
    doses = CustomDoseField(widget=CustomDoseWidget)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
