from rest_framework.viewsets import ModelViewSet
from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    # Define the queryset that this viewset will operate on.
    queryset = Order.objects.all()
    
    # Specify the serializer class to use for transforming the Order instances.
    serializer_class = OrderSerializer
