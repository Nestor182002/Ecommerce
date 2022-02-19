from django.urls import path
from ecommerce.settings import LOGOUT_REDIRECT_URL
# views
from accounts.views import LoginUser,UserRegister
# logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', UserRegister,name='register'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), {'next_page':LOGOUT_REDIRECT_URL}, name='logout'),

]


