from django.urls import path
from .views import medicines, MedicineDetailView, search_medicine, PrescriptionDetailView, \
    PrescriptionUpdateView, PrescriptionCreateView, PrescriptionDeleteView, SideEffectCreateView, \
    SideEffectDetailView, SideEffectUpdateView, SideEffectDeleteView, PrescriptionListView, PrescribedByUserListView, \
    MedicineCreateView, MedicineUpdateView, MedicineDeteleView, main_page, CurrentOrdersListView, ArchivalOrdersListView

urlpatterns = [
    path('prescription-create', PrescriptionCreateView.as_view(), name='prescription-create'),
    path('prescription-delete/<int:pk>', PrescriptionDeleteView.as_view(), name='prescription-delete'),
    path('prescription-update/<int:pk>', PrescriptionUpdateView.as_view(), name='prescription-update'),
    path('prescription-detail/<int:pk>', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescription-list/<str:valid>/<int:pk>', PrescriptionListView.as_view(), name='prescription-list'),
    path('prescription-list-by/<int:pk>', PrescribedByUserListView.as_view(), name='prescription-list-by-doctor'),
    path('prescription-list-by/<int:pk>', PrescribedByUserListView.as_view(), name='prescription-list-by-doctor'),

    path('side-effect-create', SideEffectCreateView.as_view(), name='side-effect-create'),
    path('side-effect-detail/<int:pk>', SideEffectDetailView.as_view(), name='side-effect-detail'),
    path('side-effect-update/<int:pk>', SideEffectUpdateView.as_view(), name='side-effect-update'),
    path('side-effect-delete/<int:pk>', SideEffectDeleteView.as_view(), name='side-effect-delete'),

    path('medicines', medicines, name='medicines-all'),
    path('search', search_medicine, name='search-medicine'),
    path('medicine-create', MedicineCreateView.as_view(), name='med-create'),
    path('medicines/<int:pk>', MedicineDetailView.as_view(), name='medicine-detail'),
    path('medicine-update/<int:pk>', MedicineUpdateView.as_view(), name='med-update'),
    path('medicine-delete/<int:pk>', MedicineDeteleView.as_view(), name='med-delete'),
    path('', main_page, name='index'),

    path('current-orders-list/<int:pk>/<str:state>', CurrentOrdersListView.as_view(), name='current-orders'),
    path('archival-orders-list/<int:pk>', ArchivalOrdersListView.as_view(), name='archival-orders'),
]
