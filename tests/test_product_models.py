import pytest
from product.models.category import Category
from product.models.product import Product

@pytest.mark.django_db
def test_create_category():
    # Cria uma categoria de teste
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Verifica os atributos da categoria
    assert category.name == "Electronics"  # Verifica o nome da categoria
    assert category.slug == "electronics"  # Verifica o slug da categoria
    assert category.active is True  # Garante que a categoria está ativa por padrão

@pytest.mark.django_db
def test_create_product():
    # Cria uma categoria de teste
    category = Category.objects.create(name="Electronics", slug="electronics")
    
    # Cria um produto de teste e atribui a categoria diretamente
    product = Product.objects.create(
        name="Smartphone",
        description="A high-end smartphone.",
        price=999.99,  # Preço como float para simplicidade
        stock=10,
        active=True,
        category=category  # Atribui a categoria ao produto
    )
    
    # Verifica os atributos do produto
    assert product.name == "Smartphone"  # Verifica o nome do produto
    assert product.price == 999.99  # Verifica o preço do produto
    assert product.category == category  # Verifica se a categoria foi atribuída corretamente
