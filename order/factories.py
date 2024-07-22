import factory
from django.contrib.auth.models import User
from order.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    """
    Fábrica para criar instâncias de User.
    """

    email = factory.Faker("email")
    username = factory.Faker("user_name")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    """
    Fábrica para criar instâncias de Order.
    """

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        """
        Adiciona produtos a uma ordem após a criação.
        """
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order
