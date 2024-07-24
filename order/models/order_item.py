# order/models/order_item.py
from django.db import models
from order.models import Order
from product.models import Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # Relaciona ao modelo Order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Relaciona ao modelo Product
    quantity = models.PositiveIntegerField()  # Quantidade de produtos
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order {self.order.id}"  # Representação de string
