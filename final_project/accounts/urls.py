from django.urls import path
from .views import PatientListView, PatientDetailView, \
    search_doctors, DoctorListView

urlpatterns = [
    path('patients', PatientListView.as_view(), name='patients'),
    path('doctors', DoctorListView.as_view(), name='doctors-all'),
    path('search', search_doctors, name='search-doctors')
    path('patients/<int:pk>', PatientDetailView.as_view(), name='patient-detail'),
]
