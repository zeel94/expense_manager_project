from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from .models import *
from .forms import AdminRegisterForm,UserRegisterForm,UserForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import ListView,DetailView,TemplateView
from expense.models import Expense, Category

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
    template_name = 'user/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
         logout(request)
         return redirect(reverse_lazy('login')) 

class userDashboardView(ListView):
    model = Expense
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        user = request.user
        # expenselist1 = Expense.objects.filter(user=user).values()
        expenselist = Expense.objects.filter(user=user).values('id','amount','category_id__cname','subcategory_id__scname','expdate')
        # print(expenselist)

        expense = Expense.objects.all().values()
        # expense1 = Expense.objects.all().values('amount')
        expense2 = Expense.objects.filter(user_id=request.user.id).values('amount')
        u = User.objects.all().values()
        # id = request.GET.get('id')
        budget = User.objects.filter(id=user.id).values('budget')
        print('.....................................',budget)
        userbudget = 0
        
        for b in budget:
            if b.get('budget') is not None:
                userbudget = userbudget + b.get('budget')
            print('........userbudget',userbudget)

        total = 0
        income= 0
        for i in expense2:
             total = total+i.get('amount')
             income = userbudget - total
             print('///////////income',income)

        expenselist = []  # Declare expenselist as an empty list
        for e in Expense.objects.filter(user=user).values('id','amount','category_id__cname','subcategory_id__scname','expdate'):
            expenselist.append(e)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            exp = Expense.objects.filter(category__cname__icontains=search_input).values()
            print('...................exp',exp)
            print('Search input:', search_input)
        

        return render(request, 'user/dashboard.html',{
            'expenses': expense,
            'total': total,
            'income' : income,
            'budget': userbudget,
            'expenselist': expenselist,
            # 'exp':exp
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