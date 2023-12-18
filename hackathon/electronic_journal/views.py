from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, UserRegistrationForm
from .models import User


# Create your views here.

class Login(LoginView):
    form_class = LoginForm
    template_name = 'electronic_journal/login.html'

    def get_success_url(self):
        return reverse_lazy('login')  # указать профиль


class UserRegistrationView(CreateView):
    """Регистрация"""
    model = User
    form_class = UserRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегистрированы'
    title = 'Store - Регистрация'
