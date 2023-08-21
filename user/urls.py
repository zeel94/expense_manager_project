from django import views
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('userregister/',UserRegisterView.as_view(),name='userregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('dashboard/',userDashboardView.as_view(),name='user_dashboard'),
    path('userupdate/<int:pk>',UserUpdateView.as_view(),name='userupdate'),
    path('userdetail/<int:pk>',UserDetailView.as_view(),name='userdetail'),

]
