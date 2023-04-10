from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,UserDetail

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user

class AdminRegisterForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={"class" : "input-group input-group-outline mb-3",'placeholder' : "Username"}))
    # email = forms.CharField(widget=forms.TextInput(attrs={"class" : "input-group input-group-outline mb-3",'placeholder' : "Email"}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "input-group input-group-outline mb-3",'placeholder' : "Set Password"}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "input-group input-group-outline mb-3",'placeholder' : "Confirm Password"}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')



        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_admin = True
            user.save()
            return User


class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('user','picture','phone','age','professions')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('user','picture','phone','age','professions')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user
