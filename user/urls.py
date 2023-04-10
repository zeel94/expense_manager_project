from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('userregister/',UserRegisterView.as_view(),name='userregister'),
    path('adminregister/',AdminRegisterView.as_view(),name='adminregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('dashboard/',userDashboardView.as_view(),name='user_dashboard'),
    path('userform/',UserCreateView.as_view(),name='userform'),
    path('userdetail/',UserDetailView.as_view(),name='userdetail')
]
