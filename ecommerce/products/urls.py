from django.urls import path
from products.views import ProductsView,RecentViewProduct,ListCategoryProducts,FavoriteProductPost,DetailProducts


urlpatterns = [
path('inicio/',ProductsView.as_view(),name='products'),
path('products/<int:pk>',DetailProducts,name='detail_products'),
path('recentview/',RecentViewProduct.as_view(),name='recent'),
path('favoriteproducts/<int:pk>',FavoriteProductPost,name='FavoriteP'),
path('categorys/',ListCategoryProducts.as_view(),name='category'),

]