from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact
from django.http import HttpResponseRedirect

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form, 'title': signup })

    #return render(request, 'registration/signup.html' {'form': form})

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                 #user.save()
                 login(request, user)
                 messages.success(request, "Welcome back!!!")
                 return redirect('/')
            
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required       
def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out!!")
    return redirect('/')


def contact(request):
    if request.method == "POST":
        form = Contact(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('registration/contact')
        
    else:
        form = Contact()

    return render(request, 'registration/contact.html', {'form': form})