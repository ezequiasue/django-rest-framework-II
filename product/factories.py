import factory
from product.models.category import Category
from product.models.product import Product



class CategoryFactory(factory.django.DjangoModelFactory):
    # Faker para gerpyar uma palavra realista para o nome
    name = factory.Faker("word")
    # Faker para gerar um slug realista (string amigável para URLs)
    slug = factory.Faker("slug")
    # Faker para gerar uma descrição realista
    description = factory.Faker("text")
    # Iterator para alternar entre True e False
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    # Faker para gerar um valor inteiro para o preço
    price = factory.Faker("pyint")
    # SubFactory para criar automaticamente uma instância de Category
    category = factory.SubFactory(CategoryFactory)
    # Faker para gerar uma palavra realista para o nome do produto
    name = factory.Faker("word")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        """
        Método post_generation é usado para adicionar múltiplas categorias ao produto
        após a criação inicial.

        Args:
            create (bool): Flag que indica se a instância foi criada.
            extracted (list): Lista de categorias extraídas para adicionar ao produto.
        """
        if not create:
            # Se a instância não foi criada (apenas construída), não faz nada.
            return
        if extracted:
            # Se categorias foram fornecidas, adiciona cada uma delas ao produto.
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product
