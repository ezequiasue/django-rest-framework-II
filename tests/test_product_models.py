import pytest
from product.models.category import Category
from product.models.product import Product

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(name="Electronics", slug="electronics")
    assert category.name == "Electronics"
    assert category.slug == "electronics"
    assert category.active is True

@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(name="Electronics", slug="electronics")
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,
        stock=10,
        active=True
    )
    product.category.add(category)
    assert product.name == "Smartphone"
    assert product.price == 999.99
    assert product.category.count() == 1
