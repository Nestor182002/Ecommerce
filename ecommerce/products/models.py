from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InheritedData(models.Model):
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(InheritedData):
    name=models.CharField(max_length=70)
    active=models.BooleanField(default=True)

class Products(InheritedData):
    name=models.CharField(max_length=100)
    description=models.TextField()
    img=models.ImageField(null=True,blank=True)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField(default=1)
    active=models.BooleanField(default=True)
    categorys=models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class ProductsViewRecentList(InheritedData):
    recent_user=models.ForeignKey(User,related_name='products_recent', on_delete=models.CASCADE,null=True,blank=True)
    recent_product=models.ForeignKey(Products,related_name='products_recent', on_delete=models.CASCADE)
    active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        ordering = ['-pk']
