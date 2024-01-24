from django.urls import path

from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierListAPIView, SupplierCreateAPIView, SupplierUpdateAPIView, SupplierDeleteAPIView

app_name = SuppliersConfig.name

urlpatterns = [
    path('', SupplierListAPIView.as_view(), name='suppliers'),
    path('create/', SupplierCreateAPIView.as_view(), name='create_supplier'),
    path('update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='update_supplier'),
    path('delete/<int:pk>/', SupplierDeleteAPIView.as_view(), name='delete_supplier'),
]
