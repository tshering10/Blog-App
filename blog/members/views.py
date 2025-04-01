from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
    
class UserloginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy('home')
    
class UserlogoutView(LogoutView):
    next_page = reverse_lazy('home')
    