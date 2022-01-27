from django.contrib import admin

from products.models import Products, ProductsViewRecentList

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductsViewRecentList)

