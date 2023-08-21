from django.db import models
from django.contrib.auth.models import AbstractUser
# from expense.models import Expense

# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=True,null=True)
    is_admin = models.BooleanField(default=True,null=True)
    professions = models.CharField(max_length=50,null=True)
    picture = models.ImageField(upload_to='image/',null=True,blank=True,default='media/avtar7.png')
    address = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    budget = models.IntegerField(default=0, null=True)


    class Meta:
        db_table = 'user'
    def __str__(self):
        return f"{self.username}"

# class UserDetail(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     firstname = models.CharField(max_length=50,null=True)
#     lastname = models.CharField(max_length=50,null=True)
#     email = models.EmailField(null=True)

#     class Meta:
#         db_table = 'userdetail'