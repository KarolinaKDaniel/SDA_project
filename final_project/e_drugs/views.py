import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Prescription
from accounts.models import Doctor, MyUser, Patient, Pharmacist


class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'prescription_detail.html'
    context_object_name = 'prescription'

    def get_context_data(self, **kwargs):
        context = super(PrescriptionDetailView, self).get_context_data(**kwargs)
        prescription = Prescription.objects.get(id=self.kwargs['pk'])

        patient_id = Patient.objects.get(id=prescription.patient.id)
        patient = MyUser.objects.get(username=patient_id.my_user)
        context['patient'] = f'{patient.first_name} {patient.last_name}'

        valid = prescription.created + datetime.timedelta(days=prescription.valid)
        context['filtered'] = valid

        return context


class PrescriptionListView(ListView):
    template_name = 'prescription_list.html'
    model = Prescription

    def get_context_data(self, **kwargs):
        context = super(PrescriptionListView, self).get_context_data(**kwargs)
        filtered, pk = self.kwargs['valid'], self.kwargs['pk']
        patient = Patient.objects.get(id=pk)

        if filtered == "True":
            context['prescriptions'] = Prescription.objects.filter(is_used=True, patient=patient)
        elif filtered == "False":
            context['prescriptions'] = Prescription.objects.filter(is_used=False, patient=patient)
        else:
            context['prescriptions'] = None

        return context


class PrescribedByUserListView(ListView):
    template_name = 'prescribed_by.html'
    model = Prescription

    def get_context_data(self, **kwargs):
        context = super(PrescribedByUserListView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        try:
            user = MyUser.objects.get(id=pk)
        except:
            return context

        try:
            doctor = Doctor.objects.get(my_user=user)
            context['profession'] = doctor
        except:
            try:
                pharmacist = Pharmacist.objects.get(my_user=user)
                context['profession'] = pharmacist
            except:
                context['profession'] = None

        context['prescriptions'] = Prescription.objects.filter(prescribed_by=user)
        return context
