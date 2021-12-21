from django.shortcuts import render
from django.views.generic import DetailView
from .models import Medicine

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


class DrugDetailView(DetailView):
    template_name = 'medicine_detail.html'
    model = Medicine
    context_object_name = 'medicine'
