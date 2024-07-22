import pytest
from django.contrib.auth.models import User
from order.models.order import Order
from order.models.order_item import OrderItem
from product.models.product import Product
from product.models.category import Category
from order.serializers import OrderSerializer, OrderItemSerializer

@pytest.mark.django_db
def test_order_serializer_valid():
    # Create a test user
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    # Create a test category
    category = Category.objects.create(name='Electronics', slug='electronics')
    
    # Create a test product and assign the category
    product = Product.objects.create(
        name='Smartphone',
        description='A high-end smartphone.',
        price=999.99,  # Price as a float for simplicity in this test
        stock=10,
        active=True
    )
    product.category.set([category])
    
    # Create a test order for the user
    order = Order.objects.create(user=user, status='pending')

    # Add an item to the order
    OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    
    # Serialize the order
    serializer = OrderSerializer(instance=order)
    data = serializer.data
    
    # Verify the serialized data structure
    assert len(data['items']) == 1  # Ensure there is one item
    assert data['items'][0]['product']['name'] == 'Smartphone'  # Check product name
    assert data['items'][0]['product']['description'] == 'A high-end smartphone.'  # Check product description
    assert data['items'][0]['product']['price'] == '999.99'  # Check product price
    assert data['items'][0]['product']['active'] == True  # Check product active status
    assert data['items'][0]['product']['category'][0]['name'] == 'Electronics'  # Check category name
    assert data['items'][0]['quantity'] == 2  # Verify item quantity
    assert str(data['total']) == '1999.98'  # Ensure the total is correct as a string

@pytest.mark.django_db
def test_order_item_serializer_valid():
    # Create a test user
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    # Create a test category
    category = Category.objects.create(name='Electronics', slug='electronics')
    
    # Create a test product and assign the category
    product = Product.objects.create(
        name='Smartphone',
        description='A high-end smartphone.',
        price=999.99,  # Price as a float for simplicity in this test
        stock=10,
        active=True
    )
    product.category.set([category])
    
    # Create a test order for the user
    order = Order.objects.create(user=user, status='pending')

    # Add an item to the order
    order_item = OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    
    # Serialize the order item
    serializer = OrderItemSerializer(instance=order_item)
    data = serializer.data
    
    # Verify the serialized data structure
    assert data['order_id'] == order.id  # Check the order ID
    assert data['product']['id'] == product.id  # Check the product ID
    assert data['product']['name'] == 'Smartphone'  # Check product name
    assert data['product']['description'] == 'A high-end smartphone.'  # Check product description
    assert data['product']['price'] == '999.99'  # Check product price
    assert data['product']['active'] == True  # Check product active status
    assert data['quantity'] == 2  # Verify item quantity
    assert str(data['price']) == '999.99'  # Ensure the price is correct as a string
