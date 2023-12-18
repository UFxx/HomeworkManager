from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import LoginForm


# Create your views here.

class Login(LoginView):
    form_class = LoginForm
    template_name = 'electronic_journal/login.html'

    def get_success_url(self):
        return reverse_lazy('home') #указать профиль