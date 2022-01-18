from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import PatientListView, PatientDetailView, search_doctor, DoctorListView, DoctorDetailView, \
    PatientDeleteView, CustomLoginView, RegisterPatientView, ActivateAccount, PatientUpdateView, DoctorCreateView, PharmacistCreateView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('patients', PatientListView.as_view(), name='patients'),
    path('patients/new', RegisterPatientView.as_view(), name='patient-create'),
    path('patients/<int:pk>', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/<int:pk>/edit', PatientUpdateView.as_view(), name='patient-update'),
    path('patients/<int:pk>/remove', PatientDeleteView.as_view(), name='patient-delete'),
    path('doctors', DoctorListView.as_view(), name='doctors-all'),
    path('doctors/<int:pk>', DoctorDetailView.as_view(), name='doctor-detail'),
    path('search/doctor', search_doctor, name='search-doctor'),

    path('doctor-new', DoctorCreateView.as_view(), name='doctor-create'),
    # just for the sake of creating accounts for testing
    path('pharmacist-new', PharmacistCreateView.as_view(), name='pharmacist-create'),
    # just for the sake of creating accounts for testing
]
