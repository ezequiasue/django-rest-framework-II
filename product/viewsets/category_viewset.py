from rest_framework.viewsets import ModelViewSet
from product.models import Category
from product.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD operations on Category objects.
    """
    queryset = Category.objects.all()  # Specify the queryset to retrieve all categories
    serializer_class = CategorySerializer  # Use CategorySerializer to serialize Category objects
