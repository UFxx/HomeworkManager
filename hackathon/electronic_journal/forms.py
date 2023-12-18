from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Логин", 'id': "login-input"}))
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={'placeholder': "Пароль", 'id': "login-password"}))


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Введите пароль', 'id': "registration-password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Подтвердите пароль', 'id': "repeat-registration-password"}))
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Введите имя пользователя', 'id': "username-input"}))
    group = forms.CharField(label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Введите группу', 'id': "group-input"}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Введите имя', 'id': "firstname-input"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию', 'id': "lastname-input"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес эл. почты', 'id': "email-input"}))
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона', 'id': "tel-input"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone']



class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['quest_name', 'subject', 'teacher', 'group', 'description', 'file_link', 'date_pass']

    def __init__(self, *args, **kwargs):
        super(QuestForm, self).__init__(*args, **kwargs)
