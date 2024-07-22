from rest_framework import serializers  # Import the serializers module from Django REST Framework
from product.models.product import Product  # Import the Product model from the product app
from product.serializers.category_serializer import CategorySerializer  # Import the CategorySerializer from the product app

class ProductSerializer(serializers.ModelSerializer):
    # Configure `category` to accept multiple categories (many=True) and make it required (required=True)
    category = CategorySerializer(many=True, required=True)
    
    class Meta:
        model = Product  # Define that this serializer is for the Product model
        fields = (
            "id",  # Product ID field
            "name",  # Product name field
            "description",  # Product description field
            "price",  # Product price field
            "stock",  # Product stock field
            "active",  # Product active field (whether the product is active or not)
            "category",  # Product category(ies) field
        )
        extra_kwargs = {
            'price': {'required': False},  # Define that the price field is not required
            'active': {'required': False},  # Define that the active field is not required
            'category': {'required': True}  # Reaffirm that the category field is required
        }
