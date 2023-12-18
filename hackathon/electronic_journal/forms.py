from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'placeholder': "Введите имя"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': "Введите пароль"}))
