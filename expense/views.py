from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import *
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from .forms import *

# Create your views here.
class ExpenseCreateView(CreateView):
    form_class =ExpenseForm
    model = Expense
    template_name = 'expense/expensecreate.html'
    success_url = '/expense/dashboard/'

# @method_decorator(login_required(login_url='/expense/login'),name='dispatch')

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expenselist.html'
    context_object_name = 'expenselist'


# class ExpenseDeleteView(DeleteView):
#     model = Expense
#     template_name = 'expense/expensedelete.html'
#     success_url = '/expense/list'

# class ExpenseUpdateView(UpdateView):
#     model= Expense
#     template_name = 'expense/expenseupdate.html'
#     fields = '__all__'
#     success_url = '/expense/list'

# class ExpenseDetailView(DetailView):
#     model = Expense
#     template_name = 'expense/expensedetail.html'
#     context_object_name = 'expensedetail'

def home(request):
    return render(request,'home.html')
