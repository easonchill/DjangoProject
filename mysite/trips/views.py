from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.http import FileResponse
from .red import Mkred

def hello_world(request):
    if 'user_name' in request.GET:
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render(request,'hello_world.html')


def home(request):
    post_list = Post.objects.all()
    return render(request,'home.html', {
        'post_list': post_list,
    })    

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def add1(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    Mkred(a,b,c)
    
    file=open('New_red.csv','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="New_red.csv"'
    return response


# def download(request):
#     file=open('123.txt','rb')
#     response =FileResponse(file)
#     response['Content-Type']='application/octet-stream'
#     response['Content-Disposition']='attachment;filename="'123.txt"'
#     return response