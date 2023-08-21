from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Label)
admin.site.register(Payee)
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(CurrencyType)
admin.site.register(Expense)
