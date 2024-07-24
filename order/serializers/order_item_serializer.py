from rest_framework import serializers
from order.models.order_item import OrderItem
from product.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = serializers.PrimaryKeyRelatedField(read_only=True)  # Ajuste para retornar o ID do pedido

    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'quantity', 'price')
