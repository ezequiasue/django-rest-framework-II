import pytest
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from product.models import Product, Category
from decimal import Decimal


@pytest.mark.django_db
def test_create_order():
    # Create a test user
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password"
    )

    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")

    # Create a test product and associate it with the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=Decimal("999.99"),  # Use Decimal for precise monetary values
        stock=10,
        active=True,
    )
    product.category.add(category)

    # Create a test order for the user
    order = Order.objects.create(user=user, status="pending")

    # Add an item to the order
    order_item = OrderItem.objects.create(
        order=order, product=product, quantity=2, price=product.price
    )

    # Assertions to verify the order was created correctly
    assert order.user == user  # Verify the order is associated with the correct user
    assert order.status == "pending"  # Check the order status
    assert order.items.count() == 1  # Ensure the order has one item
    assert order.items.first().product == product  # Confirm the product in the order
    assert order.items.first().quantity == 2  # Verify the quantity of the product
    assert order.items.first().price == Decimal(
        product.price
    )  # Ensure the price is correctly set


@pytest.mark.django_db
def test_order_item_creation():
    # Create a test user
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password"
    )

    # Create a test category
    category = Category.objects.create(name="Electronics", slug="electronics")

    # Create a test product and associate it with the category
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=Decimal("999.99"),  # Use Decimal for precise monetary values
        stock=10,
        active=True,
    )
    product.category.add(category)

    # Create a test order for the user
    order = Order.objects.create(user=user, status="pending")

    # Add an item to the order
    order_item = OrderItem.objects.create(
        order=order, product=product, quantity=2, price=product.price
    )

    # Assertions to verify the order item was created correctly
    assert (
        order_item.order == order
    )  # Verify the order item is associated with the correct order
    assert order_item.product == product  # Check the product in the order item
    assert order_item.quantity == 2  # Verify the quantity of the product
    assert order_item.price == Decimal(
        product.price
    )  # Ensure the price is correctly set
