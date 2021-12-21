from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Patient
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


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'

# Create your views here.
