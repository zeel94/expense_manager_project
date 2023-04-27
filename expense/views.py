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




# Create your views here.    


@method_decorator(login_required(login_url='http://127.0.0.1:8000/user/userform/'),name='dispatch')
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
    # def get(self, request, *args, **kwargs):
    #     user = UserDetail.objects.all().values()
    #     user1 = UserDetail.objects.all().values('budget')
    #     user2 = UserDetail.objects.filter(user_id=request.user.id).values('budget')
    #     expense = Expense.objects.all().values('amount') 
    #     print("user1=======",user2)

    #     for a,b in expense,user2:
    #          print(a,b)
    #          userbudget = b.get('budget') - a.get('amount')
    #     print("user budget...",userbudget)  
    #     return HttpResponse("Created...")



@method_decorator(login_required(login_url='/user/login'),name='dispatch')

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expenselist.html'
    context_object_name = 'expenselist'

    def get(self, request, *args, **kwargs):
        user = request.user
        expenselist1 = Expense.objects.filter(user=user).values()
        expenselist = Expense.objects.filter(user=user).order_by('expdate').values('id', 'amount', 'category_id__cname', 'subcategory_id__scname', 'expdate')
        # expense = Expense.objects.filter(user=user).order_by('expdate').values()
        sort_by = self.request.GET.get('sort_by', 'expdate')
        direction = self.request.GET.get('direction', 'asc')
        print(".....", sort_by)
        print(".....", direction)
        if direction == 'asc':
            expenselist = expenselist.order_by(sort_by)
        elif direction == 'desc':
            expenselist = expenselist.order_by(f'-{sort_by}')
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            expense = Expense.objects.filter(category__cname__icontains=search_input).values()
            print('...................exp',expense)
            print('Search input:', search_input)
        return render(request, 'expense/expenselist.html', {'expenselist': expenselist})

    def get_queryset(self):
        return super().get_queryset()



class ExpenseDeleteView(DeleteView):
    model = Expense
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    success_url = '/expense/list'



# class ExpenseUpdateView(UpdateView):
#     model= Expense
#     template_name = 'expense/expenseupdate.html'
#     fields = '__all__'
#     success_url = '/expense/list'

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expense/expensedetail.html'
    context_object_name = 'expensedetail'

    labels = []
    data = []
    expense = Expense.objects.all().values_list('category__cname',flat=True)
    amount = Expense.objects.all().values_list('amount',flat=True)
    for i in expense:
        labels.append(i)
    for i in amount:
        data.append(i) 

    def get(self, request, *args, **kwargs):
        user = request.user
        exp = Expense.objects.filter(id=self.kwargs['pk'],user_id=user.id)

        return render(request, self.template_name, {'expensedetail': self.get_object(),'exp':exp,'labels':self.labels,'data':self.data})

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
