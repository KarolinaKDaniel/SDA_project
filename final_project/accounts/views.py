from django.shortcuts import render
from .models import Patient, Doctor
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from e_drugs.models import Affliction
from django.urls import reverse_lazy


class PatientCreateView(CreateView):
    template_name = 'patient_form.html'
    model = Patient
    success_url = reverse_lazy('patients')



class PatientListView(ListView):
    template_name = 'patients.html'
    model = Patient
    context_object_name = 'patients'

class DoctorListView(ListView):
    template_name = 'doctors.html'
    model = Doctor
    context_object_name = 'doctors'

def search_doctors(request):
    if request.method == "POST":
        searched = request.POST['searched']
        doctors = Doctor.objects.filter(
            Q(specialization__contains=searched) | Q(my_user__last_name=searched)
        )
        return render(request, template_name='doctors.html',
                      context={"searched": searched,
                               "doctors": doctors})




class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'

# Create your views here.
