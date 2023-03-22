from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('create/',ExpenseCreateView.as_view(),name='expensecreate'),
    path('dashboard/',ExpenseListView.as_view(),name='expenselist'),
    # path('update/<int:pk>',ExpenseUpdateView.as_view(),name='expenseupdate'),
    # path('delete/<int:pk>',ExpenseDeleteView.as_view(),name='expensedelete'),
    # path('detail/<int:pk>',ExpenseDetailView.as_view(),name='expensedetail'),
    # # path('addfile/',AddFileView.as_view(),name='addfile'),
    # path('filelist/',FileListView.as_view(),name='filelist'),

]
