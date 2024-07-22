import pytest
from rest_framework.exceptions import ValidationError
from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_category_serializer_valid_data():
    category = Category.objects.create(name="Electronics", slug="electronics")
    serializer = CategorySerializer(category)
    data = serializer.data
    assert data['name'] == "Electronics"
    assert data['slug'] == "electronics"
    assert 'description' in data
    assert 'active' in data

@pytest.mark.django_db
def test_product_serializer_valid_data():
    category = Category.objects.create(name="Electronics", slug="electronics")
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,
        stock=10,
        active=True
    )
    product.category.add(category)
    serializer = ProductSerializer(product)
    data = serializer.data
    assert data['name'] == "Smartphone"
    assert data['price'] == "999.99"
    assert 'category' in data
    assert len(data['category']) == 1

@pytest.mark.django_db
def test_category_serializer_invalid_data():
    serializer = CategorySerializer(data={})
    assert not serializer.is_valid()
    assert 'name' in serializer.errors
    assert 'slug' in serializer.errors

@pytest.mark.django_db
def test_product_serializer_invalid_data():
    serializer = ProductSerializer(data={})
    assert not serializer.is_valid()
    assert 'name' in serializer.errors    
    assert 'price' not in serializer.errors # Se price for opcional, não deve estar na lista de erros
    assert 'category' in serializer.errors
