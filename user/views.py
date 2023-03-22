from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import AdminRegisterForm,UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = "/"

class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'user/admin_register.html'
    success_url = "/"


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = "expense/dashboard.html"
    

    def get_redirect_url(self):
        if self.request.user.is_authenticated:

            if self.request.user.is_admin:
                return '/'
            else:
                return '/'