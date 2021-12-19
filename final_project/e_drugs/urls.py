from django.urls import path
from .views import medicine, DrugDetailView, search_medicine

urlpatterns = [
    path('medicines', medicine, name='medicines-index'),
    path('medicines/<int:pk>', DrugDetailView.as_view(), name='medicine-detail'),
    path('search', search_medicine, name='search-medicine'),
]
