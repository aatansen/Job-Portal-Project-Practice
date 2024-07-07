from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout

# Create your views here.
def signup(request):
    if request.method=="POST":
        form=Custom_user_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form=Custom_user_form()
    context={
        'form':form
    }
    return render(request,'common/signup.html',context)

def signin(request):
    if request.method=="POST":
        form=Auth_form(request,request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form=Auth_form()
    context={
        'form':form
    }
    return render(request,'common/signin.html',context)

def dashboard(request):
    return render(request,'common/dashboard.html')

def change_password(request):
    return render(request,'common/change-password.html')