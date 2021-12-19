from django.urls import path

from .views import MedicineCreateView, MedicineUpdateView, MedicineDeteleView

urlpatterns = [
    path('medicine-create', MedicineCreateView.as_view(), name='med-create'),
    path('medicine-update/<int:pk>', MedicineUpdateView.as_view(), name='med-update'),
    path('medicine-delete/<int:pk>', MedicineDeteleView.as_view(), name='med-delete'),
    ]
