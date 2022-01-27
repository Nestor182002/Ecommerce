from django.contrib import admin
from orders.models import MyshoppingRecent, Order, OrderItem, SinglePurchase


# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SinglePurchase)
admin.site.register(MyshoppingRecent)