from django.urls import path
from . import views

urlpatterns = [
    path('mylist/', views.mylist, name='mylist'),
]