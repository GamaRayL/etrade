from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    SerializerMethodField)

from products.serializers import ProductSerialiser
from suppliers.models import Supplier
from suppliers.validators import DebtValidator


class SupplierSerializer(ModelSerializer):
    """
    Сериалайзер для Supplier(поставщика).
    Имеет два поля для удобства:
    supplier = в виде имени, а не id;
    products = основываясь на другом сериалайзере, вместо списка id
    """

    supplier = SlugRelatedField(read_only=True, slug_field='name')
    products = SerializerMethodField()

    @staticmethod
    def get_products(supplier):
        products = supplier.products.all()
        return ProductSerialiser(products, many=True).data

    class Meta:
        model = Supplier
        fields = ('id', 'name', 'email',
                  'country', 'city', 'street',
                  'house_number', 'debt', 'supplier', 'products')


class SupplierUpdateSerializer(ModelSerializer):
    """
    Сериалайзер на обновление Supplier(поставщика).
    Имеет свой валидатор, который запрещает обновление задолженности через API.
    """

    class Meta:
        model = Supplier
        fields = '__all__'

        validators = [DebtValidator(debt_field='debt')]
