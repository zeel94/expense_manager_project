from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
from expense.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('subscribe/',views.subscribe,name='subscribes'),
    path("contacts/",views.contacts,name='contacts'),
    path('create/',ExpenseCreateView.as_view(),name='expensecreate'),
    path('list/',ExpenseListView.as_view(),name='expenselist'),
    # path('chart/',ChartCreateView.as_view(),name='chart'),
    path('update/<int:pk>',ExpenseUpdateView.as_view(),name='expenseupdate'),
    path('delete/<int:pk>',ExpenseDeleteView.as_view(),name='expensedelete'),
    path('detail/<int:pk>',ExpenseDetailView.as_view(),name='expensedetail'),
    path('data/',DataListView.as_view(),name='datalist'),

    # path('profile/',profile,name="profile"),
    



]
