from django.forms import ModelForm, CharField, TextInput, Textarea, ModelMultipleChoiceField
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, MyUser
from e_drugs.models import Affliction
from django.contrib.auth.models import User
from django.db.transaction import atomic


class PatientRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']
        # add password

    address = CharField(max_length=256, widget=Textarea, min_length=20)
    phone = CharField(max_length=20, widget=TextInput)
    Personal_ID = CharField(max_length=20)
    affliction = ModelMultipleChoiceField(queryset=Affliction.objects.all(),
                                          blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        user = super().save(commit)
        address = self.cleaned_data['address']
        phone = self.cleaned_data['phone']
        Personal_ID = self.cleaned_data['Personal_ID']
        affliction = self.cleaned_data['affliction']
        my_user = MyUser(base_user=user, address=address, phone=phone, Personal_ID=Personal_ID)
        if commit:
            my_user.save()
        patient = Patient(doctor=None, my_user=my_user, affliction=affliction)
        if commit:
            patient.save()
        return user
