from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Логин", 'id': "login-input"}))
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={'placeholder': "Пароль", 'id': "login-password"}))


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    group = forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите группу'})
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите номер телефона'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
