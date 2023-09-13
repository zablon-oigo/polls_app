from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *

def sign_in(request):
    if request.method =='GET':
        return render(request, 'login.html',{
            'form':LoginForm(),
        })
    elif request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login was successfull')
                return redirect('vote:home')
        messages.error(request, 'Invalid username or Password')
        return render(request,'login.html',{'form':form})
    
def sign_out(request):
    logout(request)
    messages.success(request,'Logout was successfull')
    return redirect('vote:home')

def sign_up(request):
    if request.method=='GET':
        return render(request, 'reg.html',{
            'form':RegForm(),
        })
    
    elif request.method =='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,"The sign up was successfull")
            login(request, user)
            return redirect('vote:home')
        else:
            messages.error(request,'Plase correct the following errors ')
            return render(request, 'reg.html',{'form':form})

