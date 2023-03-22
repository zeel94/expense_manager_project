import django.forms as form
from .models import Expense
from expense.models import Expense

class ExpenseForm(form.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

