from django.urls import path
from products.views import ProductsView,ListCategoryProducts,DetailProducts,FavoriteProductPost,RecentViewProduct,FavoriteProductPage


urlpatterns = [
path('inicio/',ProductsView.as_view(),name='products'),
path('products/<int:pk>',DetailProducts,name='detail_products'),
path('recentview/',RecentViewProduct.as_view(),name='recent'),
path('favoriteproducts/<int:pk>',FavoriteProductPost,name='FavoriteP'),
path('categorys/',ListCategoryProducts.as_view(),name='category'),
path('favoritepage/',FavoriteProductPage.as_view(),name='FavoritePage'),

]