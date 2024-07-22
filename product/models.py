from django.db import models
from django.contrib.auth.models import User

class Brand(models.TextChoices):
    LG = 'LG'
    SAMSUNG = 'SAMSUNG'
    APPLE = 'APPLE'
    XIAOMI = 'XIAOMI'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    brand = models.CharField(max_length=20, choices=Brand.choices)  # Set an appropriate max_length
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
