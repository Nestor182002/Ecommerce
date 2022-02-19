
from django.contrib.auth.forms import UserCreationForm
from django import forms
# user
from django.contrib.auth.models import User



class UserCreateForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Contraseña de confirmacion',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
