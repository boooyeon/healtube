from django.urls import path
from . import views
from django.contrib.auth.models import User
from django.contrib import auth

urlpatterns = [
     path('mylist',  views.SaveForm, name='mylist'),
     path('mylist/searchresult', views.SearchFormView, name='searchresult'),
     path('mylist/search/', views.Search, name='search')
]