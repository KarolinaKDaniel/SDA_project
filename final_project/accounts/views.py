from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View, UpdateView
from .forms import PatientRegistrationForm, DoctorCreationForm, PharmacistCreationForm, PatientUpdateForm
from django.shortcuts import redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib import messages
from .tokens import account_activation_token
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Patient, Doctor, User, MyUser


class PatientUpdateView(UpdateView):
    template_name = 'patient_form.html'
    model = Patient
    form_class = PatientUpdateForm
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        my_user_pk = Patient.objects.get(pk=self.kwargs.get('pk')).my_user.pk
        base_user_pk = MyUser.objects.get(pk = my_user_pk).base_user.pk
        user = User.objects.get(pk = base_user_pk)
        return user

    def get_initial(self):
        initial_data = super().get_initial()
        patient = Patient.objects.get(pk=self.kwargs.get('pk'))
        initial_data['address'] = patient.my_user.address
        initial_data['phone'] = patient.my_user.phone
        initial_data['personal_ID'] = patient.my_user.Personal_ID
        initial_data['affliction'] = patient.affliction.all()
        initial_data['doctor'] = patient.doctor.all()
        return initial_data


class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = MyUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.base_user.is_active = True
            user.base_user.save()
            login(request, user.base_user)
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


class RegisterPatientView(CreateView):
    template_name = 'patient_form.html'
    form_class = PatientRegistrationForm
    success_url = reverse_lazy('index')


class DoctorCreateView(CreateView):
    template_name = 'patient_form.html'
    form_class = DoctorCreationForm
    success_url = reverse_lazy('index')


class PharmacistCreateView(CreateView):
    template_name = 'patient_form.html'
    form_class = PharmacistCreationForm
    success_url = reverse_lazy('index')


class CustomLoginView(LoginView):
    template_name = 'login.html'


class PatientCreateView(CreateView):
    template_name = 'patient_form.html'
    model = Patient
    success_url = reverse_lazy('patients')


class PatientDeleteView(CreateView):
    template_name = 'patient_delete.html'
    model = Patient
    success_url = reverse_lazy('patients')


class PatientListView(ListView):
    template_name = 'patients.html'
    model = Patient
    context_object_name = 'patients'


class DoctorDetailView(DetailView):
    template_name = "doctor_detail.html"
    model = Doctor
    context_object_name = "doctor"


class DoctorListView(ListView):
    template_name = 'doctors.html'
    paginate_by = 3
    model = Doctor
    context_object_name = 'doctors'


def search_doctor(request):
    if request.method == "POST":
        searched = request.POST['searched']
        doctors = Doctor.objects.filter(
            Q(specialization__icontains=searched) | Q(my_user__base_user__last_name__icontains=searched)
        )
        return render(request, template_name='doctors.html',
                      context={"searched": searched,
                               "doctors": doctors})


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'

# Create your views here.
