from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import MedicineForm
from .models import Medicine


class MedicineCreateView(CreateView):
    form_class = MedicineForm
    template_name = 'form.html'
    success_url = reverse_lazy('patients')


class MedicineUpdateView(UpdateView):
    form_class = MedicineForm
    template_name = 'form.html'
    success_url = reverse_lazy('patients')


class MedicineDeteleView(DeleteView):
    template_name = 'medicine_delete.html'
    model = Medicine
    success_url = reverse_lazy('patients')
