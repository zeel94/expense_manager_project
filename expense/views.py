from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from user.models import *
from django.db.models import Sum





# Create your views here.    


# @method_decorator(login_required(login_url='http://127.0.0.1:8000/user/userform/'),name='dispatch')
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    form_class =ExpenseForm
    model = Expense
    template_name = 'expense/expensecreate.html'
    success_url = '/user/dashboard/'


    def form_valid(self, form):
        return super().form_valid(form)
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        subject = "Welcome to Mysite"
        message = "Hello Guys! you just created your expense. Thank you for joining us."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email]        
        send_mail(subject, message, email_from, recipient_list)
        return response
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

@method_decorator(login_required(login_url='/user/login'),name='dispatch')

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expenselist.html'
    context_object_name = 'expenselist'

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
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            expenselist = expenselist.filter(category__cname__icontains=search_input)
        return render(request, 'expense/expenselist.html', {'expenselist': expenselist, 'expense': expense})

    def get_queryset(self):
        return super().get_queryset()



class ExpenseDeleteView(DeleteView):
    model = Expense
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    success_url = '/expense/list'



class ExpenseUpdateView(UpdateView):
    model= Expense
    template_name = 'expense/expenseupdate.html'
    fields = ['amount','category','subcategory','paymentMethod','description']
    success_url = '/expense/list'

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expense/expensedetail.html'
    context_object_name = 'expensedetail'

    def get(self, request, *args, **kwargs):
        # Filter expenses by current user
        expenses = Expense.objects.filter(user=request.user)

        # Aggregate expenses by category and sum their amounts
        expense_totals = expenses.values('category__cname').annotate(total=Sum('amount'))

        # Initialize labels and data lists
        labels = []
        data = []

        # Loop through expenses and add category names and amounts to lists
        for expense in expense_totals:
            labels.append(expense['category__cname'])
            data.append(expense['total'])

        # Pass labels and data to chart configuration
        chart_labels = {'labels': labels}
        chart_data = {'data': data}

        context = {'expensedetail': self.get_object(),
                   'expenses': expenses,
                   'chart_labels': chart_labels,
                   'chart_data': chart_data}

        return render(request, self.template_name, context)
    
def home(request):
    return render(request,'home.html')

  

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail( 
            'Thank you for contacting us', #title
            'You have a new message from Expense Manager Website regarding '+subject,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False  

        )

        messages.info(request,'your message has been send successfully.')

    return redirect('http://127.0.0.1:8000/')

def subscribe(request):
    if request.method == 'POST':
        message = 'Thank you for connecting with us. You will get notified about all the updates of the Expense Manager website.'
        email = request.POST['email']

        send_mail( 
            'Subscription of Expense Manager', #title
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False  

        )

        messages.info(request,'Your message has been send successfully .')

    return redirect('http://127.0.0.1:8000/')

class DataListView(ListView):
    model = Expense
    template_name = 'expense/datadetail.html'
    context_object_name = 'datalist'
