from django.forms import ModelForm, CharField, TextInput, Textarea, ModelMultipleChoiceField, MultipleHiddenInput, ImageField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .models import Patient, MyUser, Doctor
from e_drugs.models import Affliction
from django.contrib.auth.models import User
from django.db.transaction import atomic
from .tokens import account_activation_token


class PatientUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
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
        user = super().save(commit)
        address = self.cleaned_data['address']
        phone = self.cleaned_data['phone']
        Personal_ID = self.cleaned_data['Personal_ID']
        affliction = self.cleaned_data['affliction']
        doctor = self.cleaned_data['doctor']
        my_user = MyUser.objects.get(base_user__pk=user.pk)
        my_user.address = address
        my_user.phone = phone
        my_user.Personal_ID = Personal_ID
        if commit:
            my_user.save()
        patient = Patient.objects.get(my_user__pk=my_user.pk)
        for doc in doctor:
            patient.doctor.add(doc)
        for afflic in affliction:
            patient.affliction.add(afflic)
        if commit:
            patient.save()
        return user


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
        html_email_template = get_template('account_activation_email.html')
        d = {'username': user.username,
             'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
             'token': account_activation_token.make_token(my_user),}
        subject, from_email, to = 'welcome', 'test@test.pl', user.email
        html_content = html_email_template.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return user


class PharmacistCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

    address = CharField(max_length=256, widget=Textarea, min_length=20)
    phone = CharField(max_length=20, widget=TextInput)
    Personal_ID = CharField(max_length=20)
    credential_id = CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        address = self.cleaned_data['address']
        phone = self.cleaned_data['phone']
        Personal_ID = self.cleaned_data['Personal_ID']
        credential_id = self.cleaned_data['credential_id']

        my_user = MyUser(base_user=user, address=address, phone=phone, Personal_ID=Personal_ID)
        if commit:
            my_user.save()
        pharmacist = Pharmacist(my_user=my_user, credential_id=credential_id)
        if commit:
            pharmacist.save()

        return user

class DoctorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

    address = CharField(max_length=256, widget=Textarea, min_length=20)
    phone = CharField(max_length=20, widget=TextInput)
    Personal_ID = CharField(max_length=20)
    credential_id = CharField(max_length=128)
    photo = ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        address = self.cleaned_data['address']
        phone = self.cleaned_data['phone']
        Personal_ID = self.cleaned_data['Personal_ID']
        credential_id = self.cleaned_data['credential_id']
        photo = self.cleaned_data['photo']
        my_user = MyUser(base_user=user, address=address, phone=phone, Personal_ID=Personal_ID)
        if commit:
            my_user.save()
        doctor = Doctor(my_user=my_user, credential_id=credential_id, photo=photo)
        if commit:
            doctor.save()

        return user
