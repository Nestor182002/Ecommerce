from django.urls import path

from products.views import ProductsView,DetailProducts


urlpatterns = [
path('inicio/',ProductsView.as_view(),name='products'),
path('products/<int:pk>',DetailProducts.as_view(),name='detail_products')
]