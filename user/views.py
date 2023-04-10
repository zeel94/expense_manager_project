from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User,UserDetail
from .forms import AdminRegisterForm,UserRegisterForm,UserForm,UserDetailForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView,DetailView
from expense.models import Expense

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = "http://127.0.0.1:8000/user/login/"

class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'user/admin_register.html'
    success_url = "/"


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = "user/dashboard.html"
    

    def get_redirect_url(self):
        if self.request.user.is_authenticated:

            if self.request.user.is_admin:
                return 'http://127.0.0.1:8000/user/dashboard/'
            else:
                return '/'
class UserLogoutView(LogoutView):
    # template_name = 'user/login.html'
    next_page=None
    http_method_names = ["get", "head", "post", "options"]


class userDashboardView(ListView):            
    
    def get(self, request, *args, **kwargs):
        expense = Expense.objects.all().values()
        
        return render(request, 'user/dashboard.html',{
            'expenses':expense,
        })

    template_name = 'user/dashboard.html'


class UserCreateView(CreateView):
    form_class = UserForm
    model = UserDetail
    template_name = 'user/user.html'
    success_url = 'user/userdetail.html'

class UserDetailView(ListView):
    form_class = UserDetailForm
    model = UserDetail
    template_name = 'user/userdetail.html'
    context_object_name = 'userdetail'

