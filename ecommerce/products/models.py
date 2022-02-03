from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    img=models.ImageField(null=True,blank=True)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField(default=1)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name



class ProductsViewRecentList(models.Model):
    recent_user=models.ForeignKey(User,related_name='products_recent', on_delete=models.CASCADE,null=True,blank=True)
    recent_product=models.ForeignKey(Products,related_name='products_recent', on_delete=models.CASCADE)
    active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        ordering = ['-pk']
