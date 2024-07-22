from rest_framework import serializers
from order.models.order import Order
from order.models.order_item import OrderItem
from order.serializers.order_item_serializer import OrderItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "user",
            "status",
            "items",
            "total",
        )

    def get_items(self, instance):
        order_items = OrderItem.objects.filter(order=instance)
        return OrderItemSerializer(order_items, many=True).data

    def get_total(self, instance):
        order_items = OrderItem.objects.filter(order=instance)
        total = sum(item.price * item.quantity for item in order_items)
        return total
