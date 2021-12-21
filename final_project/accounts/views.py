from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Patient, Doctor
from django.db.models import Q


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



