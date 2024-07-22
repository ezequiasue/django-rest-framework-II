from rest_framework import serializers
from order.models.order_item import OrderItem
from product.serializers.product_serializer import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id')  # Serialize the order ID
    product = ProductSerializer()  # Serialize the product details

    class Meta:
        model = OrderItem
        fields = (
            "order_id",  # Include the order ID
            "product",
            "quantity",
            "price",
        )
