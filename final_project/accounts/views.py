from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Patient


class PatientListView(ListView):
    template_name = 'patients.html'
    model = Patient
    context_object_name = 'patients'


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'

# Create your views here.
