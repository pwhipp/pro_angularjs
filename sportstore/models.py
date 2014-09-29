from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits=8, decimal_places=2)
