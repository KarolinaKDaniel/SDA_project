from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import PatientListView, PatientDetailView, search_doctor, DoctorListView, DoctorDetailView, CustomLoginView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('patients', PatientListView.as_view(), name='patients'),
    path('patients/<int:pk>', PatientDetailView.as_view(), name='patient-detail'),
    path('doctors', DoctorListView.as_view(), name='doctors-all'),
    path('doctors/<int:pk>', DoctorDetailView.as_view(), name='doctor-detail'),
    path('search/doctor', search_doctor, name='search-doctor'),
]
