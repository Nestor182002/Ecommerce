from django.db import models

from products.models import Products
from django.contrib.auth.models import User

SHOPPING_IN = [
        ('pp', 'paypal'),
        ('wp', 'whatsapp'),
]

# Create your models here.
class Order(models.Model):
    order_user=models.ForeignKey(User,related_name="order_user",on_delete=models.CASCADE,null=True,blank=True)
    complete=models.BooleanField(default=False)
    order_for_wp=models.BooleanField(default=False)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.order_user
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name="order",on_delete=models.CASCADE)
    order_product=models.ForeignKey(Products,related_name="order_products",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.order}-{self.order_product}"

class SinglePurchase(models.Model):
    single_products=models.ForeignKey(Products,related_name="single_product",on_delete=models.CASCADE)
    of_orderitem=models.ForeignKey(OrderItem,related_name="single_orderitem",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.single_products}-{self.of_orderitem}"

class MyshoppingRecent(models.Model):
    shopping_user=models.ForeignKey(User,related_name="shopping_user",on_delete=models.CASCADE,null=True,blank=True)
    shopping_order=models.ForeignKey(Order,related_name="shopping",on_delete=models.CASCADE,null=True,blank=True)
    singlepurchase=models.ForeignKey(SinglePurchase,related_name="single_purchase",on_delete=models.CASCADE,null=True,blank=True)
    shopping_in=models.CharField(choices=SHOPPING_IN,max_length=100)

    def __str__(self):
        return f"{self.shopping_user}-{self.shopping_order}"

    

