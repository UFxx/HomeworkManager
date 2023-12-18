from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from hackathon.electronic_journal.forms import UserRegistrationForm
from hackathon.electronic_journal.models import User


# Create your views here.

def index(request):
    return render(request, 'electronic_journal/index.html')


class UserRegistrationView(CreateView):
    """Регистрация"""
    model = User
    form_class = UserRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегистрированы'
    title = 'Store - Регистрация'
