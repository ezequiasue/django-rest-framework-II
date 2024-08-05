from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.permissions import AllowAny


class ProductViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD operations on Product objects.
    """
    queryset = Product.objects.all() # Queryset to retrieve all Order objects
    serializer_class = ProductSerializer # Serializer for Order objects

    #authentication_classes = [BasicAuthentication, SessionAuthentication]  # Authentication methods used
    permission_classes = [AllowAny]  # Not Required permissions
