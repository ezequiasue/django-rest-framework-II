from rest_framework import serializers
from order.models.order_item import OrderItem
from product.serializers.product_serializer import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id')  # Adiciona o ID do pedido
    product = ProductSerializer()  # Serializa o produto

    class Meta:
        model = OrderItem
        fields = (
            "order_id",  # Inclua o ID do pedido
            "product",
            "quantity",
            "price",
        )
