from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered! Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})


def user_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            print("radiko abaan")
            return redirect('dashboard')  
        else:
            messages.error(request, "Invalid credentials, please try again.")
            print("Login error message set.")
    return render(request, "registration/login.html")


def user_logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')