from django.forms import ModelForm, Form
from .models import Patient, MyUser


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


class CombinedFormBase(Form):
    form_classes = []

    def __init__(self, *args, **kwargs):
        super().__init__()
        for f in self.form_classes:
            name = f.__name__.lower()
            setattr(self, name, f(*args, **kwargs))
            form = getattr(self, name)
            self.fields.update(form.fields)
            self.initial.update(form.initial)


class PatientRegistrationForm(CombinedFormBase):
    form_classes = [MyUserForm, PatientForm]