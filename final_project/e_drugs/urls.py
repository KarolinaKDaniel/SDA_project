from django.urls import path
from .views import PrescriptionDetailView, PrescriptionListView, PrescribedByUserListView

urlpatterns = [
    path('prescription-detail/<int:pk>', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescription-list/<str:valid>/<int:pk>', PrescriptionListView.as_view(), name='prescription-list'),
    path('prescription-list-by/<int:pk>', PrescribedByUserListView.as_view(), name='prescription-list-by-doctor')
]
