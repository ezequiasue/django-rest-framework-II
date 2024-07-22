import pytest
from django.contrib.auth.models import User
from order.models.order import Order
from order.models.order_item import OrderItem
from product.models.product import Product
from product.models.category import Category
from order.serializers import OrderSerializer, OrderItemSerializer

@pytest.mark.django_db
def test_order_serializer_valid():
    # Cria um usuário de teste
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    # Cria uma categoria de teste
    category = Category.objects.create(name='Electronics', slug='electronics')
    
    # Cria um produto e atribui a categoria
    product = Product.objects.create(
        name='Smartphone',
        description='A high-end smartphone.',
        price=999.99,
        stock=10,
        active=True
    )
    product.category.set([category])
    
    # Cria um pedido
    order = Order.objects.create(user=user, status='pending')

    # Adiciona um item ao pedido
    OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    
    # Serializa o pedido
    serializer = OrderSerializer(instance=order)
    data = serializer.data
    
    # Verifica a estrutura dos dados serializados
    assert len(data['items']) == 1  # Verifica que há um item
    assert data['items'][0]['product']['name'] == 'Smartphone'
    assert data['items'][0]['product']['description'] == 'A high-end smartphone.'
    assert data['items'][0]['product']['price'] == '999.99'
    assert data['items'][0]['product']['active'] == True
    assert data['items'][0]['product']['category'][0]['name'] == 'Electronics'  # Verifica a categoria
    assert data['items'][0]['quantity'] == 2
    assert str(data['total']) == '1999.98'  # Garante que o total é comparado como string

@pytest.mark.django_db
def test_order_item_serializer_valid():
    # Cria um usuário de teste
    user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    # Cria uma categoria de teste
    category = Category.objects.create(name='Electronics', slug='electronics')
    
    # Cria um produto e atribui a categoria
    product = Product.objects.create(
        name='Smartphone',
        description='A high-end smartphone.',
        price=999.99,
        stock=10,
        active=True
    )
    product.category.set([category])
    
    # Cria um pedido
    order = Order.objects.create(user=user, status='pending')

    # Adiciona um item ao pedido
    order_item = OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    
    # Serializa o item do pedido
    serializer = OrderItemSerializer(instance=order_item)
    data = serializer.data
    
    # Verifica a estrutura dos dados serializados
    assert data['order_id'] == order.id  # Verifica o ID do pedido
    assert data['product']['id'] == product.id  # Verifica o ID do produto
    assert data['product']['name'] == 'Smartphone'
    assert data['product']['description'] == 'A high-end smartphone.'
    assert data['product']['price'] == '999.99'
    assert data['product']['active'] == True
    assert data['quantity'] == 2
    assert str(data['price']) == '999.99'  # Garante que o preço é comparado como string
