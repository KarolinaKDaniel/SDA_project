import datetime
from logging import getLogger

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import MedicineForm, PrescriptionForm, SideEffectForm, MedicineInstanceForm, OrderForm
from .models import Prescription, Medicine, SideEffect, Order, MedicineInstance
from accounts.models import Doctor, MyUser, Patient, Pharmacist

from cart.forms import CartAddProductForm

LOGGER = getLogger(__name__)


def main_page(request):
    return render(request, template_name='main_page.html', context={'medicines': Medicine.objects.all(),
                                                                    'doctors': Doctor.objects.all()})


def medicines(request):
    sorting = request.GET.get('s', 'default')
    if sorting == "name":
        drugs_list = Medicine.objects.all().order_by("name")
    elif sorting == "price_net":
        drugs_list = Medicine.objects.all().order_by("price_net")
    else:
        drugs_list = Medicine.objects.all()
    paginator = Paginator(drugs_list, 3)
    page = request.GET.get('page')
    try:
        meds = paginator.page(page)
    except PageNotAnInteger:
        meds = paginator.page(1)
    except EmptyPage:
        meds = paginator.page(paginator.num_pages)
    return render(request, template_name='medicines.html', context={'medicines': meds,
                                                                    'page': page})

def search_medicine(request):
    if request.method == "POST":
        searched = request.POST['searched']
        medicines = Medicine.objects.filter(
            Q(substance__name__contains=searched) | Q(name__contains=searched),
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

    def get_context_data(self, **kwargs):
        context = super(MedicineDetailView, self).get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()

        medicine_instance_count = MedicineInstance.objects.filter(medicine=self.kwargs.get('pk')).count()
        cart_product_form.fields['quantity'].choices = [(i, str(i)) for i in range(1, medicine_instance_count+1)]

        context['cart_product_form'] = cart_product_form
        context['medicine_instance_count'] = medicine_instance_count

        return context


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
        context['patient_id'] = int(patient_id.id)

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


class OrderCreateView(CreateView):
    form_class = OrderForm
    success_url = reverse_lazy("index")
    template_name = 'order_form.html'

    def get_initial(self):
        initial = super(OrderCreateView, self).get_initial()
        # patient = Patient.objects.get(my_user=self.request.user.id)
        # print(patient.first_name)
        if self.request.user.is_authenticated:
            initial.update({'patient': self.request.user.id})
        return initial


class PrescriptionCreateView(CreateView):
    form_class = PrescriptionForm
    template_name = 'prescription_form.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
        initial = super(PrescriptionCreateView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'prescribed_by': self.request.user.id})
        return initial


class PrescriptionUpdateView(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'prescription_form.html'
    success_url = reverse_lazy('index')


class PrescriptionDeleteView(DeleteView):
    template_name = 'prescription_delete.html'
    model = Prescription
    success_url = reverse_lazy('index')


class SideEffectCreateView(CreateView):
    form_class = SideEffectForm
    template_name = 'side_effect_form.html'
    success_url = reverse_lazy('index')


class SideEffectDetailView(DetailView):
    template_name = 'side_effect_detail.html'
    model = SideEffect
    context_object_name = 'side_effect'


class SideEffectUpdateView(UpdateView):
    model = SideEffect
    form_class = SideEffectForm
    template_name = 'side_effect_form.html'
    success_url = reverse_lazy('index')


class SideEffectDeleteView(DeleteView):
    template_name = 'side_effect_delete.html'
    model = SideEffect
    success_url = reverse_lazy('index')


class CurrentOrdersListView(ListView):
    template_name = 'current_orders_list.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state, pk = self.kwargs['state'], self.kwargs['pk']
        patient = Patient.objects.get(id=pk)

        if state == 'accepted':
            queryset = Order.objects.filter(patient=patient, state='accepted')
        elif state == 'paid':
            queryset = Order.objects.filter(patient=patient, state='paid')
        elif state == 'processed':
            queryset = Order.objects.filter(patient=patient, state='processed')
        elif state == 'shipped':
            queryset = Order.objects.filter(patient=patient, state='shipped')[:1]
        else:
            queryset = None
        context['orders'] = queryset

        return context


class ArchivalOrdersListView(ListView):
    template_name = 'archival_orders_list.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(id=self.kwargs['pk'])

        archival_order_list = Order.objects.filter(state='shipped', patient=patient)

        context['orders'] = archival_order_list
        context['patient'] = patient

        return context


class OrdersByStateListView(ListView):
    template_name = 'orders_by_state_list.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state = self.kwargs['state']

        if state == 'accepted':
            queryset = Order.objects.filter(state='accepted')
        elif state == 'paid':
            queryset = Order.objects.filter(state='paid')
        elif state == 'processed':
            queryset = Order.objects.filter(state='processed')
        elif state == 'shipped':
            queryset = Order.objects.filter(state='shipped')
        else:
            queryset = None
        context['orders'] = queryset

        return context


class OrderDetailView(DetailView):
    template_name = 'order_detail.html'
    model = Order
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(id=self.kwargs['pk'])

        patient = Patient.objects.get(id=order.patient.id)
        context['patient'] = patient
        context['order'] = order

        return context


class MedicineInstanceCreateView(CreateView):
    form_class = MedicineInstanceForm
    template_name = 'med_inst_form.html'

    def form_valid(self, form):
        how_many = form.cleaned_data["quantity"]
        for i in range(how_many):
            product = MedicineInstance(
                medicine=form.cleaned_data['medicine'],
                expire_date=form.cleaned_data['expire_date'],
                code=form.cleaned_data['code']
            )
            product.save()
        return HttpResponseRedirect(reverse_lazy('index'))


class MedicineInstanceUpdateView(UpdateView):
    model = MedicineInstance
    form_class = MedicineInstanceForm
    template_name = 'med_inst_form.html'
    success_url = reverse_lazy('index')


class MedicineInstanceDeleteView(DeleteView):
    template_name = 'med_inst_delete.html'
    model = MedicineInstance
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        self.object = self.get_object()
        form = self.get_form()
        data = request.POST['fulltextarea']
        LOGGER.info(f'Id: {self.object.id}-{self.object.medicine.name}:{self.object.code} '
                    f'is deleted by id:{user.id} {user.first_name} {user.last_name} with reason: {data}')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
