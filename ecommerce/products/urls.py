from django.urls import path

from products.views import ProductsView,DetailProducts,RecentViewProduct


urlpatterns = [
path('inicio/',ProductsView.as_view(),name='products'),
path('products/<int:pk>',DetailProducts,name='detail_products'),
path('recentview/',RecentViewProduct.as_view(),name='recent')
]