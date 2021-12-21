from django.urls import path
from .views import medicines, DrugDetailView, search_medicine, PrescriptionDetailView, \
    PrescriptionListView, PrescribedByUserListView

urlpatterns = [
    path('medicines', medicines, name='medicine-all'),
    path('medicines/<int:pk>', DrugDetailView.as_view(), name='medicine-detail'),
    path('search', search_medicine, name='search-medicine'),
    path('prescription-detail/<int:pk>', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescription-list/<str:valid>/<int:pk>', PrescriptionListView.as_view(), name='prescription-list'),
    path('prescription-list-by/<int:pk>', PrescribedByUserListView.as_view(), name='prescription-list-by-doctor')
]
