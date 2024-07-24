from django.db import models
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=255)  # Nome do produto
    description = models.TextField()  # Descrição do produto
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))  # Preço do produto
    stock = models.PositiveIntegerField()  # Quantidade em estoque
    active = models.BooleanField(default=True)  # Status ativo do produto
    category = models.ForeignKey("Category", related_name="products", on_delete=models.CASCADE)  # Categoria relacionada
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora de atualização

    def __str__(self):
        return self.name  # Representação do produto como string
