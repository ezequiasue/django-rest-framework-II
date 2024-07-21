from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()
    
    
    def get_total(self, instance):
        total = sum([Product.price for product in instance.product.all()])
        return total
    
    
    class Meta:
        model = Product
        fields = ['product', 'total']

# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = ('id', 'product', 'quantity', 'price')

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True, read_only=True)  # Nested serializer for OrderItem

#     class Meta:
#         model = Order
#         fields = ('id', 'user', 'status', 'created_at', 'updated_at', 'items')


