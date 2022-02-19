from django.urls import path
# views
from accounts.views import LoginUser,UserRegister

urlpatterns = [
    path('register/', UserRegister,name='register'),
    path('login/',LoginUser.as_view(),name='login')
]


