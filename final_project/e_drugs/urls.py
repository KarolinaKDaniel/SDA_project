from django.urls import path

from .views import MedicineCreateView, MedicineUpdateView, MedicineDeteleView

urlpatterns = [
    path('medicine-create', MedicineCreateView.as_view(), name='med-create'),
    path('medicine-update', MedicineUpdateView.as_view(), name='med-update'),
    path('medicine-delete', MedicineDeteleView.as_view(), name='med-delete'),
    ]
