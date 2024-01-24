from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerialiser(ModelSerializer):
    """Сериалайзер продукта"""

    class Meta:
        model = Product
        fields = '__all__'
