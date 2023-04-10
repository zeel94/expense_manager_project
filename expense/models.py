from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=50)
    class Meta:
        db_table = 'category'
    def __str__(self):
        return self.cname


class SubCategory(models.Model):
    scname = models.CharField(max_length=50)
    cid = models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        db_table = 'subcategory'
    def __str__(self):
        return self.scname


class Label(models.Model):
    lname = models.CharField(max_length=50)
    class Meta:
        db_table = 'label'
    def __str__(self):
        return self.lname
    


class Payee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'payee'
    def __str__(self):
        return self.name


typename = ('creditcard','CreditCard'),('cash','Cash'),('bank','Bank')
class AccountType(models.Model):
    type_name = models.CharField(choices=typename,max_length=50)

    class Meta:
        db_table = 'accounttype'
    def __str__(self):
        return self.type_name

class CurrencyType(models.Model):
    curreny = models.CharField(max_length=50)
    class Meta:
        db_table = 'currencytype'
    def __str__(self):
        return self.curreny

class Account(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.IntegerField()
    currency_type = models.ForeignKey(CurrencyType,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType,on_delete=models.CASCADE)
    class Meta:
        db_table = 'account'
    def __str__(self):
        return self.balance




paymentMethod = ('cash','Cash'),('cheque','Cheque'),('creditcard','CreditCard')
status = ('cleared','Cleared'),('uncleared','UnCleared'),('void','Void')
class Expense(models.Model):
    amount = models.IntegerField()
    expdate = models.DateField(auto_now_add=True)
    exptime = models.TimeField(auto_now_add=True,null=True)
    payee = models.ForeignKey(Payee,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    paymentMethod = models.CharField(choices=paymentMethod,max_length=50) 
    status = models.CharField(choices=status,max_length=50)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'expense'
    def __str__(self):
        return str(self.category)
