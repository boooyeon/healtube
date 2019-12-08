from django.shortcuts import render
from django.http import HttpResponse
from .models import Channel

# Create your views here.
def home(request):
    return render(request, 'main/home.html')



def get_list_by_user(request, username):
    print("username : ", username)
    return HttpResponse("{}의 블로그 글 리스트가 출력됩니다!".format(username))