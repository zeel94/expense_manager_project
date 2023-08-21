from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        strip=False,
        widget=forms.TextInput,
    )
    email = forms.CharField(
        label="Email",
        strip=False,
        widget=forms.EmailInput,
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Repeat Password",
        strip=False,
        widget=forms.PasswordInput,
        help_text='Password should be 8 character long'

    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')


    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_user = True
    #     user.save()
    #     return user



class UserForm(forms.ModelForm):
    username = forms.CharField(
        label="Username",
        strip=False,
        widget=forms.TextInput,
    )

    class Meta():
        model = User
        fields = ('username','last_name','first_name','age','professions','budget','picture','email','address')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user


# class UserDetailForm(forms.ModelForm):
#     class Meta:
#         model = UserDetail
#         fields = ('user','firstname','lastname','age','professions','budget')


#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_user = True
#         user.save()
#         return user
