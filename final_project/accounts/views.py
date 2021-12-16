from django.shortcuts import render
from django.views.generic import ListView
from .models import Patient


class PatientListView(ListView):
    template_name = 'patients.html'
    model = Patient
    context_object_name = 'patients'

# Create your views here.
