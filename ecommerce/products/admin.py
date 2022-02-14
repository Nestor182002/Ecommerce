from django.contrib import admin
from products.models import Products, ProductsViewRecentList,Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(ProductsViewRecentList)

