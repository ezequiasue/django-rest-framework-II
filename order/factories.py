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
from django.contrib.auth.models import User
from order.models import Order
from product.factories import ProductFactory
from order.models import OrderItem

class UserFactory(factory.django.DjangoModelFactory):
    """
    Fábrica para criar instâncias de User.
    """
    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall('set_password', 'password123')

    class Meta:
        model = User

class OrderFactory(factory.django.DjangoModelFactory):
    """
    Fábrica para criar instâncias de Order.
    """
    user = factory.SubFactory(UserFactory)  # Cria um usuário associado

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        """
        Adiciona OrderItems a uma ordem após a criação.
        """
        if not create:
            return

        if extracted:
            for product, quantity, price in extracted:
                OrderItem.objects.create(order=self, product=product, quantity=quantity, price=price)

    class Meta:
        model = Order

# Execução do script para criar uma ordem com itens
if __name__ == "__main__":
    from product.factories import ProductFactory

    # Cria alguns produtos
    products = ProductFactory.create_batch(3)  # Cria 3 produtos

    # Cria uma ordem e associa esses produtos com quantidades e preços
    items = [(product, 2, 19.99) for product in products]  # Exemplo: 2 unidades de cada produto, preço 19.99
    order = OrderFactory(items=items)
    print(order)

