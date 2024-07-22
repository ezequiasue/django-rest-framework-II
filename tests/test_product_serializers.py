import pytest
from rest_framework.exceptions import ValidationError
from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_category_serializer_valid_data():
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Serialize the category instance
    serializer = CategorySerializer(category)
    data = serializer.data
    
    # Validate serialized data
    assert data['name'] == "Electronics"  # Check category name
    assert data['slug'] == "electronics"  # Check category slug
    assert 'description' in data  # Ensure description is included
    assert 'active' in data  # Ensure active is included

@pytest.mark.django_db
def test_product_serializer_valid_data():
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Create a test product and assign the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,
        stock=10,
        active=True
    )
    product.category.add(category)
    
    # Serialize the product instance
    serializer = ProductSerializer(product)
    data = serializer.data
    
    # Validate serialized data
    assert data['name'] == "Smartphone"  # Check product name
    assert data['price'] == "999.99"  # Check product price (string format)
    assert 'category' in data  # Ensure category is included
    assert len(data['category']) == 1  # Verify the category count

@pytest.mark.django_db
def test_category_serializer_invalid_data():
    # Test serializer with invalid data
    serializer = CategorySerializer(data={})
    assert not serializer.is_valid()  # Ensure serializer is invalid
    assert 'name' in serializer.errors  # Check 'name' field error
    assert 'slug' in serializer.errors  # Check 'slug' field error

@pytest.mark.django_db
def test_product_serializer_invalid_data():
    # Test serializer with invalid data
    serializer = ProductSerializer(data={})
    assert not serializer.is_valid()  # Ensure serializer is invalid
    assert 'name' in serializer.errors  # Check 'name' field error
    assert 'price' not in serializer.errors  # If price is optional, it should not be in errors
    assert 'category' in serializer.errors  # Check 'category' field error
