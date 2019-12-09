from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django import forms
from main.models import Channel


def Search(request):
    return render(request, 'mylist/search.html')

def mylist(request):
    return render(request, 'mylist/mylist.html',)

def SearchFormView(request):
    rq = request
    print(rq)
    sort1 = request.GET.get('sort-select1','')
    sort2 = request.GET.get('sort-select2','')
    # queryset=Channel.objects.all()
    # for row in queryset.values_list():
    #     print(row)
    
    # print(sort1)
    # print(sort2)
    # queryset = Channel.objects.all()
    # for row in queryset.values_list():
    #     print (row)
    Channel.objects.all()
    obs = Channel.objects.filter(health_type = sort1, health_part = sort2).only("channel_name", "health_type", "health_part", "video_title", "video_link", "video_view_num", "video_upload_date")
    
    context = {'obs':obs}


    # a = []
    # for row in ob.values():
    #    a.append(row)
    #    print(a)
    
    # for i in a:
    #     print(i.keys())
    #     print(i.values())



    # print(queryset)
    # for channel_instance in queryset:
    #      print(channel_instance)
    
    return render(request,'mylist/searchresult.html' , context)



def SaveForm(request):
    rq = request
    choices = request.GET.getlist('chk_info') # list

    print(choices)
    checklist = []
    for i in choices:
        obs2 = Channel.objects.filter(id=i)
        checklist.append(obs2)
 
    context2 = {'checklist':checklist}

    print(checklist) 
    print(context2)
    return render(request, 'mylist/mylist.html' , context2)
    # for i in choices:
    #     print(i)
       
    #     Channel.objects.all()
    #     basket = Channel.objects.filter(id=i)
    #     print(basket)

    # context2 = {'basket':basket}
    
    
    
    
    # 현재 로그인되어 있는 유저 정보를 가져와서
    # user = User.objects.get(id=user_id)
    # # 저기 channels list일꺼 같은데
    # # 그러면 for문 돌려서
    # for channel_id in channels:
    #         channel = Channel.objects.get(
    #            id=channel_id
    #         )
    #         user.cart.add(Channel)
    # # cart 객체들만 갖고와서 
    # # 아래 페이지에 전달

# def post(request):
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
      


       


   

