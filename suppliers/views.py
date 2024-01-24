from rest_framework import filters, status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from suppliers.models import Supplier
from suppliers.permissions import IsUserActive
from suppliers.serializers import SupplierSerializer, SupplierUpdateSerializer


class SupplierListAPIView(ListAPIView):
    """Получение списка поставщиков"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']

    permission_classes = [IsUserActive]


class SupplierCreateAPIView(CreateAPIView):
    """Создание поставщика"""
    serializer_class = SupplierSerializer
    permission_classes = [IsUserActive]


class SupplierUpdateAPIView(UpdateAPIView):
    """Обновление поставщика"""
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializer
    permission_classes = [IsUserActive]


class SupplierDeleteAPIView(DestroyAPIView):
    """Удаление поставщика"""
    queryset = Supplier.objects.all()
    permission_classes = [IsUserActive]

    def delete(self, request, *args, **kwargs):
        supplier = self.get_object()
        supplier.delete()

        return Response(
            {'message': 'Привычка удалена.'},
            status=status.HTTP_204_NO_CONTENT
        )
