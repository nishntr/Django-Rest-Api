from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)
    stocks = models.IntegerField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
