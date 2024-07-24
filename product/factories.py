import os
import sys
import django

# Adicione o caminho do projeto ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Inicialize o Django
django.setup()

import factory
from product.models.category import Category
from product.models.product import Product

class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")  # Gera um nome realista
    slug = factory.Faker("slug")  # Gera um slug realista
    description = factory.Faker("text")  # Gera uma descrição realista
    active = factory.Iterator([True, False])  # Alterna entre True e False

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")  # Gera um nome de produto realista
    description = factory.Faker("text")  # Gera uma descrição de produto realista
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)  # Gera um preço realista
    stock = factory.Faker("pyint")  # Gera uma quantidade em estoque realista
    active = factory.Iterator([True, False])  # Alterna entre True e False
    category = factory.SubFactory(CategoryFactory)  # Cria automaticamente uma instância de Categoria

    class Meta:
        model = Product

if __name__ == "__main__":
    # Cria 5 categorias e 10 produtos
    for _ in range(5):
        CategoryFactory()

    for _ in range(10):
        ProductFactory()

    print("Categorias e produtos criados com sucesso!")
