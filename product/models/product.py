# product/models.py

from django.db import models  # Import Django's model module
from decimal import Decimal  # Import Decimal for precise decimal numbers

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # Product price
    stock = models.IntegerField()  # Product stock
    active = models.BooleanField(default=True)  # Product active status
    category = models.ManyToManyField('Category', related_name='products')  # Related categories
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return self.name  # String representation of the product
