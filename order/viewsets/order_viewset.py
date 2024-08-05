from rest_framework.viewsets import ModelViewSet
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class OrderViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD operations on Order objects.
    """
    queryset = Order.objects.all()  # Fetch all Order instances
    serializer_class = OrderSerializer  # Serializer for Order objects

    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]  # Supported authentication methods
    permission_classes = [IsAuthenticated, IsAdminUser]  # Access requires authentication and admin rights
