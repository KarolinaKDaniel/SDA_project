from django.urls import path

from .views import MedicineCreateView

urlpatterns = [
    path('medicine-create', MedicineCreateView.as_view(), name='med-create'),
]
