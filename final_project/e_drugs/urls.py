from django.urls import path
from .views import medicines, DrugDetailView, search_medicine, PrescriptionDetailView, \
    PrescriptionListView, PrescribedByUserListView,main_page

urlpatterns = [
    path('medicines', medicines, name='medicines-all'),
    path('medicines/<int:pk>', DrugDetailView.as_view(), name='medicine-detail'),
    path('search', search_medicine, name='search-medicine'),
    path('prescription-detail/<int:pk>', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescription-list/<str:valid>/<int:pk>', PrescriptionListView.as_view(), name='prescription-list'),
    path('prescription-list-by/<int:pk>', PrescribedByUserListView.as_view(), name='prescription-list-by-doctor'),
    path('', main_page, name='index')
]
