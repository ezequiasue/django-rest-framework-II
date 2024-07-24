from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD operations on Product objects.
    """
    queryset = Product.objects.all()  # Define the queryset to retrieve all products
    serializer_class = ProductSerializer  # Use ProductSerializer to handle serialization and deserialization of Product objects
