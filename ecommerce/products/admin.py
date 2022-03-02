from django.contrib import admin
from products.models import Products, ProductsViewRecentList,Category,ProductsFavorite

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display= ('name','price','quantity','created','active')
    list_filter = ('price','active')
    search_fields = ['name', 'price',]
    

admin.site.register(Category)
admin.site.register(Products,ProductsAdmin)
admin.site.register(ProductsViewRecentList)
admin.site.register(ProductsFavorite)


