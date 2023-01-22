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


class BasketItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return f'Products for {self.user}'

    class Meta:
        ordering = ['user']


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ForeignKey(BasketItem, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Basket for {self.user}'

    class Meta:
        ordering = ['user']