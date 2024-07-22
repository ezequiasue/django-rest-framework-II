import pytest
from product.models.category import Category
from product.models.product import Product

@pytest.mark.django_db
def test_create_category():
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Verify the category attributes
    assert category.name == "Electronics"  # Check category name
    assert category.slug == "electronics"  # Check category slug
    assert category.active is True  # Ensure category is active by default

@pytest.mark.django_db
def test_create_product():
    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Create a test product and assign the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,  # Price as a float for simplicity
        stock=10,
        active=True
    )
    product.category.add(category)
    
    # Verify the product attributes
    assert product.name == "Smartphone"  # Check product name
    assert product.price == 999.99  # Check product price
    assert product.category.count() == 1  # Ensure the product has one category assigned
