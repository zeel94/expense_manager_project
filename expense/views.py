from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import *
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
# class ExpenseCreateView(CreateView):
#     form_class =ExpenseForm
#     model = Expense
#     template_name = 'expense/expensecreate.html'
#     success_url = '/user/dashboard/'

#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             print(user,"User--------------")
#             subject = "welcome to django"
#             message = "hello django"
#             email_from = settings.EMAIL_HOST_USER
#             email = [user.email]
#             recipient_list = email
#             print(email," email ---------------------------------------------")
#             res = send_mail(subject,message,email_from,recipient_list)
#             print(res," mail info---------------------------------------------")
#         return super(ExpenseCreateView, self.user).form_valid(form)
    

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    form_class =ExpenseForm
    model = Expense
    template_name = 'expense/expensecreate.html'
    success_url = '/user/dashboard/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        subject = "Welcome to Mysite"
        message = "Hello Guys! you just created your expense. Thank you for join us."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email]        
        send_mail(subject, message, email_from, recipient_list)
        return response



# @method_decorator(login_required(login_url='/expense/login'),name='dispatch')

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expenselist.html'
    context_object_name = 'expenselist'
    ordering = ['-expdate']
    



class ExpenseDeleteView(DeleteView):
    model = Expense
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    # template_name = 'expense/expensedelete.html'
    success_url = '/expense/list'



# class ExpenseUpdateView(UpdateView):
#     model= Expense
#     template_name = 'expense/expenseupdate.html'
#  bv   fields = '__all__'
#     success_url = '/expense/list'

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expense/expensedetail.html'
    context_object_name = 'expensedetail'

    labels = []
    data = []
    expense = Expense.objects.all().values_list('category',flat=True)
    amount = Expense.objects.all().values_list('amount',flat=True)
    for i in expense:
        labels.append(i)
    for i in amount:
        data.append(i) 

    def get(self, request, *args, **kwargs):
        exp = Expense.objects.filter(id=self.kwargs['pk'])
        return render(request, self.template_name, {'expensedetail': self.get_object(),'exp':exp,'labels':self.labels,'data':self.data})

def home(request):
    return render(request,'home.html')


    
