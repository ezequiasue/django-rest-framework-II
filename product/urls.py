# product/urls.py
from django.urls import path, include
from rest_framework import routers
from product.viewsets.category_viewset import CategoryViewSet
from product.viewsets.product_viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
