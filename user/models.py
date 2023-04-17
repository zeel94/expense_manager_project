from django.db import models
from django.contrib.auth.models import AbstractUser
# from expense.models import Expense

# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=True,null=True)
    is_admin = models.BooleanField(default=True,null=True)

    class Meta:
        db_table = 'user'

class UserDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,null=True)
    lastname = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    professions = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='image',null=True,blank=True)
    phone = models.IntegerField(null=True)
    age = models.IntegerField()
    budget = models.IntegerField(null=True)
    # USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'userdetail'