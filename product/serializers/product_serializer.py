from rest_framework import serializers
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer  # Importar o serializer da categoria

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Usar CategorySerializer para serializar a categoria

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "stock",
            "active",
            "category",
        )
        extra_kwargs = {
            'price': {'required': False},
            'active': {'required': False},
            'category': {'required': True}
        }
