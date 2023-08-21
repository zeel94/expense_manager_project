from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from .models import *
from .forms import UserRegisterForm,UserForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView,DetailView,TemplateView
from expense.models import Expense, Category
from django.core.mail import send_mail
from django.conf import settings


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = "http://127.0.0.1:8000/user/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        subject = "Welcome"
        message = "Hello! You can create and manage your expenses here. Thank you for joining us."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]        
        send_mail(subject, message, email_from, recipient_list)
        return response


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = "user/dashboard.html"
    

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
                return 'http://127.0.0.1:8000/user/dashboard/'
        
        
class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
         logout(request)
         return redirect(reverse_lazy('login')) 

class userDashboardView(ListView):
    model = Expense
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        user = request.user
        expenselist = Expense.objects.filter(user=user).order_by('expdate').values('id', 'amount', 'category_id__cname', 'subcategory', 'expdate')
        sort_by = self.request.GET.get('sort_by', 'exptime')
        direction = self.request.GET.get('direction', 'asc')
        expense = []
        if direction == 'asc':
            expenselist = expenselist.order_by(sort_by)
        else:
            expenselist = expenselist.order_by(f'-{sort_by}')
        
        expense = Expense.objects.filter(user_id=request.user.id).values('amount')
        
        budget = User.objects.filter(id=user.id).values('budget')
        userbudget = 0
        
        for b in budget:
            if b.get('budget') is not None:
                userbudget = userbudget + b.get('budget')

        total = 0
        income= 0
        for i in expense:
             total = total+i.get('amount')
             income = userbudget - total

        expenselist_filtered = expenselist  # Make a copy of expenselist
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            expenselist_filtered = expenselist.filter(category__cname__icontains=search_input)

        return render(request, 'user/dashboard.html',{
            'expenses': expense,
            'total': total,
            'income' : income,
            'budget': userbudget,
            'expenselist': expenselist_filtered,
        })

    template_name = 'user/dashboard.html'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/user.html'
    success_url = 'user/userdetail.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user/userdetail.html'
    context_object_name = 'userdetail'

class UserUpdateView(UpdateView):
    model= User
    form_class = UserForm
    template_name = 'user/userupdate.html'
    # success_url = '/user/userdetail'

    def get_success_url(self):
        return reverse_lazy('userdetail', kwargs={'pk':self.object.pk})