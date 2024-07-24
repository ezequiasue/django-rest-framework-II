import pytest
from rest_framework.exceptions import ValidationError
from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_category_serializer_valid_data():
    # Cria uma categoria de teste
    category = Category.objects.create(name="Electronics", slug="electronics", description="Devices and gadgets")
    
    # Serializa a instância da categoria
    serializer = CategorySerializer(category)
    data = serializer.data
    
    # Valida os dados serializados
    assert data['name'] == "Electronics"  # Verifica o nome da categoria
    assert data['slug'] == "electronics"  # Verifica o slug da categoria
    assert data['description'] == "Devices and gadgets"  # Verifica a descrição da categoria
    assert data['active'] is True  # Verifica se a categoria está ativa

@pytest.mark.django_db
def test_product_serializer_valid_data():
    # Cria uma categoria de teste
    category = Category.objects.create(name="Electronics", slug="electronics", description="A category for electronics")
    
    # Cria um produto de teste e atribui a categoria
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,
        stock=10,
        active=True,
        category=category  # Atribui a categoria diretamente
    )
    
    # Serializa a instância do produto
    serializer = ProductSerializer(product)
    data = serializer.data
    
    # Valida os dados serializados
    assert data['name'] == "Smartphone"  # Verifica o nome do produto
    assert data['price'] == "999.99"  # Verifica o preço do produto (formato string)
    assert data['category']['id'] == category.id  # Verifica o ID da categoria
    assert data['category']['name'] == category.name  # Verifica o nome da categoria
    assert data['category']['slug'] == category.slug  # Verifica o slug da categoria


@pytest.mark.django_db
def test_category_serializer_invalid_data():
    # Testa o serializer com dados inválidos
    serializer = CategorySerializer(data={})
    assert not serializer.is_valid()  # Garante que o serializer é inválido
    assert 'name' in serializer.errors  # Verifica erro no campo 'name'
    assert 'slug' in serializer.errors  # Verifica erro no campo 'slug'

@pytest.mark.django_db
def test_product_serializer_invalid_data():
    # Testa o serializer com dados inválidos
    serializer = ProductSerializer(data={})
    assert not serializer.is_valid()  # Garante que o serializer é inválido
    assert 'name' in serializer.errors  # Verifica erro no campo 'name'
    assert 'category' in serializer.errors  # Verifica erro no campo 'category'
    assert 'description' in serializer.errors  # Verifica erro no campo 'description'
    assert 'stock' in serializer.errors  # Verifica erro no campo 'stock'
    # Não verificamos 'price' aqui porque é opcional
