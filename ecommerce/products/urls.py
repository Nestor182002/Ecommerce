from django.urls import path

from products.views import ProductsView


urlpatterns = [
path('inicio/',ProductsView.as_view(),name='products')
]