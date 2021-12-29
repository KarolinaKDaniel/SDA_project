from django.urls import path
from .views import medicines, MedicineDetailView, search_medicine, PrescriptionDetailView, \
    PrescriptionListView, PrescribedByUserListView, MedicineCreateView, MedicineUpdateView, MedicineDeteleView, \
    main_page, CurrentOrdersListView, ArchivalOrdersListView, OrdersByStateListView, OrderDetailView

urlpatterns = [
    path('medicines', medicines, name='medicines-all'),
    path('medicines/<int:pk>', MedicineDetailView.as_view(), name='medicine-detail'),
    path('search', search_medicine, name='search-medicine'),
    path('prescription-detail/<int:pk>', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescription-list/<str:valid>/<int:pk>', PrescriptionListView.as_view(), name='prescription-list'),
    path('prescription-list-by/<int:pk>', PrescribedByUserListView.as_view(), name='prescription-list-by-doctor'),
    path('', main_page, name='index'),
    path('prescription-list-by/<int:pk>', PrescribedByUserListView.as_view(), name='prescription-list-by-doctor'),
    path('medicine-create', MedicineCreateView.as_view(), name='med-create'),
    path('medicine-update/<int:pk>', MedicineUpdateView.as_view(), name='med-update'),
    path('medicine-delete/<int:pk>', MedicineDeteleView.as_view(), name='med-delete'),
    path('current-orders-list/<int:pk>/<str:state>', CurrentOrdersListView.as_view(), name='current-orders'),
    path('archival-orders-list/<int:pk>', ArchivalOrdersListView.as_view(), name='archival-orders'),
    path('orders-list/<str:state>', OrdersByStateListView.as_view(), name='orders-list'),
    path('order-detail/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
]
