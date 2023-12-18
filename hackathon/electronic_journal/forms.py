from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Логин", 'id': "login-input"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': "Пароль", 'id': "login-password"}))
