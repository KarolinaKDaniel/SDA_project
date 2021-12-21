from django.urls import path
from .views import medicines, DrugDetailView, search_medicine

urlpatterns = [
    path('medicines', medicines, name='medicine-all'),
    path('medicines/<int:pk>', DrugDetailView.as_view(), name='medicine-detail'),
    path('search', search_medicine, name='search-medicine'),
]
