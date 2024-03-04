from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')

def login_user(request):

    # error = False
    # valid = False

    # if request.method == "POST":
    #     name = request.POST["username"]
    #     pwd = request.POST["password"]

    #     try:
    #         user = authenticate(username = name, password = pwd)
    #     except:
    #         error = True   
    #     try:
    #         if user:
    #             login(request,user)
    #             valid = True
    #     except:
    #         error = True
    
    # dic = {'error':error,'valid':valid}

    return render(request,'login.html')

def login_user(request):

    # error = False
    # valid = False

    # if request.method == "POST":
    #     name = request.POST["username"]
    #     pwd = request.POST["password"]

    #     try:
    #         user = authenticate(username = name, password = pwd)
    #     except:
    #         error = True   
    #     try:
    #         if user:
    #             login(request,user)
    #             valid = True
    #     except:
    #         error = True
    
    # dic = {'error':error,'valid':valid}

    return render(request,'login.html')

def register(request):
    return render(request,'register.html')