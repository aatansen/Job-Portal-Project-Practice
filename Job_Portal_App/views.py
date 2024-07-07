from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from notifications.signals import notify

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

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

def change_password(request):
    if request.method == 'POST':
        old_password=request.POST.get('old_password')
        new_password=request.POST.get('new_password')
        new_confirm_password=request.POST.get('new_confirm_password')
        
        checking=check_password(old_password,request.user.password)
        if checking:
            if new_password==new_confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                notify.send(sender=request.user,recipient=request.user,verb='you have changed your password recently')
                update_session_auth_hash(request,request.user)
                return redirect('dashboard')
    return render(request,'common/change-password.html')

def all_notifications(request):
    notifications=request.user.notifications.all()

    context={
        'notifications':notifications
    }

    return render(request,'common/all-notifications.html',context)