from rest_framework import serializers
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    # Configurar `category` para aceitar listas de categorias e tornar obrigatório
    category = CategorySerializer(many=True, required=True)
    
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "stock",  # Adicione 'stock' se for relevante
            "active",
            "category",
        )
        extra_kwargs = {
            'price': {'required': False},  # Se price for opcional
            'active': {'required': False},  # Se active for opcional
            'category': {'required': True}  # Se category for obrigatório
        }
