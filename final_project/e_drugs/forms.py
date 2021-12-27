import json

from django.forms import ModelForm
from django.template.loader import render_to_string

from .models import Medicine


class MedicineForm(ModelForm):

    class Meta:
        model = Medicine
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
