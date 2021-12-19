from django.shortcuts import render
from django.views.generic import CreateView

from .forms import MedicineForm
from .models import Medicine

class MedicineCreateView(CreateView):

    form_class = MedicineForm
    template_name = 'form.html'
