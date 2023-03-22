from django.contrib import admin
from django.urls import path
from .views import UserRegisterView,AdminRegisterView,UserLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('userregister/',UserRegisterView.as_view(),name='useregister'),
    path('adminregister/',AdminRegisterView.as_view(),name='adminregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]
