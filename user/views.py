import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login as loginsession


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_num = request.POST.get('phone')
        email = request.POST.get('address')
        User.objects.create_user(username=username, password=password, phone=phone_num, address=email)
        return redirect('users:login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            loginsession(request, user)

            return redirect('users:home')
        else:
            return HttpResponse('로그인 실패')

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
        
    
       
    


     
