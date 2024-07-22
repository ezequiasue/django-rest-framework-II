import pytest
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from product.models import Product, Category
from decimal import Decimal

@pytest.mark.django_db
def test_create_order():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
    category = Category.objects.create(name='Electronics', slug='electronics')
    product = Product.objects.create(
        name='Smartphone',
        description='A high-end smartphone.',
        price=Decimal('999.99'),  # Use Decimal for precision
        stock=10,
        active=True
    )
    product.category.add(category)
    
    # Criar o pedido
    order = Order.objects.create(user=user, status='pending')
    
    # Adicionar itens ao pedido
    order_item = OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    
    # Testar o pedido
    assert order.user == user
    assert order.status == 'pending'
    assert order.items.count() == 1
    assert order.items.first().product == product
    assert order.items.first().quantity == 2
    assert order.items.first().price == Decimal(product.price)  # Compare Decimal with Decimal

@pytest.mark.django_db
def test_order_item_creation():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
    category = Category.objects.create(name='Electronics', slug='electronics')
    product = Product.objects.create(
        name='Smartphone',
        description='A high-end smartphone.',
        price=Decimal('999.99'),  # Use Decimal for precision
        stock=10,
        active=True
    )
    product.category.add(category)
    
    # Criar o pedido
    order = Order.objects.create(user=user, status='pending')
    
    # Adicionar itens ao pedido
    order_item = OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    
    # Testar o item do pedido
    assert order_item.order == order
    assert order_item.product == product
    assert order_item.quantity == 2
    assert order_item.price == Decimal(product.price)  # Compare Decimal with Decimal
