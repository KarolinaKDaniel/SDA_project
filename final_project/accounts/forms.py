from django.forms import ModelForm
from .models import Patient, MyUser
from betterforms.multiform import MultiModelForm
from django.utils.encoding import python_2_unicode_compatible


class MyUserForm(ModelForm):

    class Meta:
        model = MyUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyUserCreationMultiForm(MultiModelForm):
    form_class = {
        'my_user': MyUserForm,
        'patient': PatientForm,
    }