import django.forms as forms
from .models import Expense
from expense.models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount','category','subcategory','paymentMethod','status','description','user')
        widgets = {
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user

class ChartForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('category',)
