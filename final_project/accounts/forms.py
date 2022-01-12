from django.forms import ModelForm, CharField, TextInput, Textarea, ModelMultipleChoiceField, MultipleHiddenInput
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, MyUser, Doctor
from e_drugs.models import Affliction
from django.contrib.auth.models import User
from django.db.transaction import atomic


class PatientRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

    address = CharField(max_length=256, widget=Textarea, min_length=20)
    phone = CharField(max_length=20, widget=TextInput)
    Personal_ID = CharField(max_length=20)
    affliction = ModelMultipleChoiceField(queryset=Affliction.objects.all(),
                                          blank=True, required=False)
    doctor = ModelMultipleChoiceField(queryset=Doctor.objects.all(), widget=MultipleHiddenInput, required=False, blank=True)

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
        print(affliction)
        doctor = self.cleaned_data['doctor']
        my_user = MyUser(base_user=user, address=address, phone=phone, Personal_ID=Personal_ID)
        if commit:
            my_user.save()
        patient = Patient(my_user=my_user)
        if commit:
            patient.save()
            for doc in doctor:
                patient.doctor.add(doc)
            for afflic in affliction:
                patient.affliction.add(afflic)
        return user
