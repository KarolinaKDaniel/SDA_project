from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import MyUserCreationMultiForm
from django.shortcuts import redirect

from .models import Patient, Doctor


class CustomLoginView(LoginView):
    template_name = 'login.html'

class PatientCreateView(CreateView):
    form_class = MyUserCreationMultiForm
    template_name = 'patient_form.html'
    success_url = reverse_lazy('patients')

    def form_valid(self, form):
        my_user = form['my_user'].save()
        patient = form['patient'].save(commit=False)
        patient.my_user = my_user
        patient.save()
        return redirect(self.get_success_url())


# class PatientUpdateView(UpdateView):
#     model = Patient
#     form_class = PatientRegistrationForm
#     template_name = 'patient_form.html'
#     success_url = reverse_lazy('patients')


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_delete.html'
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
    model = Doctor
    context_object_name = 'doctors'


def search_doctor(request):
    if request.method == "POST":
        searched = request.POST['searched']
        doctors = Doctor.objects.filter(
            Q(specialization__icontains=searched) | Q(my_user__last_name__icontains=searched)
        )
        return render(request, template_name='doctors.html',
                      context={"searched": searched,
                               "doctors": doctors})


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'

# Create your views here.
