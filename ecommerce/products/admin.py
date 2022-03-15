from django.contrib import admin
from products.models import Products, ProductsViewRecentList,Category,ProductsFavorite

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('pk','name','active')
    list_filter = ('name','active')
    search_fields = ['name']

class ProductsAdmin(admin.ModelAdmin):
    list_display= ('pk','name','price','quantity','created','active')
    list_filter = ('categorys','price','active')
    search_fields = ['name', 'price',]

class ProductsViewRecentListAdmin(admin.ModelAdmin):
    list_display= ('pk','recent_user','recent_product','active')
   
class FavoriteAdmin(admin.ModelAdmin):
    list_display= ('pk','favorite_user','favorite_product')
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(ProductsViewRecentList,ProductsViewRecentListAdmin)
admin.site.register(ProductsFavorite,FavoriteAdmin)


