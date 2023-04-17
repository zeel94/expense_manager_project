from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
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
                return 'http://127.0.0.1:8000/user/dashboard/'
        
        
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

def form_valid(self, form):
        # create a Payee object for the logged-in user if it doesn't exist
        payee, created = Payee.objects.get_or_create(user=self.request.user, defaults={'name': self.request.user.username})

        # set the payee field of the Expense object to the Payee instance
        form.instance.payee = payee
        form.instance.save()

        # subject = 'Alert Expense/Income Added'
        # message = 'We are pleased to inform you that your recent income/expense has been added successfully to your Expense Manager App. Your updated records are now available for you to access and review at any time.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [self.request.user.email]
        # send_mail(subject, message, email_from, recipient_list)
        
        return super().form_valid(form)
