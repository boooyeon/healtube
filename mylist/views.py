from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django import forms
from main.models import Channel


def Search(request):
    return render(request, 'mylist/search.html')

def mylist(request):
    return render(request, 'mylist.html',)

def SearchFormView(request):
    rq = request
    print(rq)
    sort1 = request.GET.get('sort-select1','')
    sort2 = request.GET.get('sort-select2','')
    # queryset=Channel.objects.all()
    # for row in queryset.values_list():
    #     print(row)
    
    print(sort1)
    print(sort2)
    # queryset = Channel.objects.all()
    # for row in queryset.values_list():
    #     print (row)
    Channel.objects.all()
    ob = Channel.objects.filter(health_type = sort1, health_part = sort2)
    print (ob)

    a = []
    for row in ob.values_list():
       a.append(row)
       print(a)
      
    # print(queryset)
    # for channel_instance in queryset:
    #      print(channel_instance)
    
    return render(request,'mylist/searchresult.html' , {'a' : a})
 
# def searchpost(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_vaild():
#             search = form.save(commit=False)
#             search.save
#             return redirect('search')

#     else:
#         form = SearchForm()
#         return render(request, 'searchresult.html',{'form':form})
# Create your views here.
      


       


   

