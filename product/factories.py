import factory
from product.models.category import Category
from product.models.product import Product

class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")  # Generate a realistic name
    slug = factory.Faker("slug")  # Generate a realistic slug
    description = factory.Faker("text")  # Generate a realistic description
    active = factory.Iterator([True, False])  # Alternate between True and False

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")  # Generate an integer price
    category = factory.SubFactory(CategoryFactory)  # Automatically create a Category instance
    name = factory.Faker("word")  # Generate a realistic product name

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)  # Add categories to the product

    class Meta:
        model = Product
