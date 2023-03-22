from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True,null=True)
    # picture = models.ImageField(upload_to='image'.null=True,blank=True)
    class Meta:
        db_table = 'user'

