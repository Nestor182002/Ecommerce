from django.urls import reverse
from django.shortcuts import redirect, render
# form
from forms.UserRegisterForm import UserCreateForm
# loginView
from django.contrib.auth.views import LoginView


# Create your views here.

def UserRegister(request):
    if request.method == "POST":
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('products'))
    else:
        form=UserCreateForm()
    context={'forms':form}
    return render(request,'loginform/register.html',context)


class LoginUser(LoginView):
    template_name = 'loginform/login.html'