from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Patient
from e_drugs.models import Affliction


class PatientListView(ListView):
    template_name = 'patients.html'
    model = Patient
    context_object_name = 'patients'


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients'] = Affliction.objects.all()
        return context

# Create your views here.
