from django.db import models
from store.validators import validate_file_size
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


class Promotion(models.Model):
    title = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', validators=[validate_file_size])
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(1)])
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')
    promotions = models.ManyToManyField(Promotion, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f'Basket for {self.user}'

    class Meta:
        ordering = ['user']


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True, related_name='items')

    def __str__(self) -> str:
        return f'Products for {self.basket}'

    class Meta:
        ordering = ['basket']