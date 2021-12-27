import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import MedicineForm, PrescriptionForm, SideEffectForm
from .models import Prescription, Medicine, SideEffect
from accounts.models import Doctor, MyUser, Patient, Pharmacist


def main_page(request):
    return render(request, template_name='main_page.html')


def medicines(request):
    sorting = request.GET.get('s', 'default')
    if sorting == "name":
        drugs_list = Medicine.objects.all().order_by("name")
    elif sorting == "price_net":
        drugs_list = Medicine.objects.all().order_by("price_net")
    else:
        drugs_list = Medicine.objects.all()
    return render(request, template_name='medicines.html', context={'medicines': drugs_list})


def search_medicine(request):
    if request.method == "POST":
        searched = request.POST['searched']
        medicines = Medicine.objects.filter(
            substance__name__contains=searched,
            substance__is_active=True
        )
        return render(request, template_name='medicines.html',
                      context={"searched": searched,
                               "medicines": medicines})


class MedicineCreateView(CreateView):
    form_class = MedicineForm
    template_name = 'medicine_form.html'
    success_url = reverse_lazy('medicines-all')


class MedicineDetailView(DetailView):
    template_name = 'medicine_detail.html'
    model = Medicine
    context_object_name = 'medicine'


class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine_form.html'
    success_url = reverse_lazy('medicines-all')


class MedicineDeteleView(DeleteView):
    template_name = 'medicine_delete.html'
    model = Medicine
    success_url = reverse_lazy('medicines-all')


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


class PrescriptionCreateView(CreateView):
    form_class = PrescriptionForm
    template_name = 'prescription_forms.html'
    success_url = reverse_lazy('index')


class PrescriptionUpdateView(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'prescription_forms.html'
    success_url = reverse_lazy('index')


class PrescriptionDeleteView(DeleteView):
    template_name = 'prescription_delete.html'
    model = Prescription
    success_url = reverse_lazy('index')


class SideEffectCreateView(CreateView):
    form_class = SideEffectForm
    template_name = 'side_effect_forms.html'
    success_url = reverse_lazy('index')


class SideEffectDetailView(DetailView):
    template_name = 'side_effect_detail.html'
    model = SideEffect
    context_object_name = 'side_effect'


class SideEffectUpdateView(UpdateView):
    model = SideEffect
    form_class = SideEffectForm
    template_name = 'side_effect_forms.html'
    success_url = reverse_lazy('index')


class SideEffectDeleteView(DeleteView):
    template_name = 'side_effect_delete.html'
    model = SideEffect
    success_url = reverse_lazy('index')
