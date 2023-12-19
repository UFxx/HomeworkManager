from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import LoginForm, UserRegistrationForm
from .models import Quest, UserQuest, User


class Login(LoginView):
    form_class = LoginForm
    template_name = 'electronic_journal/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')  # указать профиль


class UserRegistrationView(CreateView):
    """Регистрация"""
    model = get_user_model()
    form_class = UserRegistrationForm
    template_name = 'electronic_journal/registration.html'

    def get_success_url(self):
        return reverse_lazy('login')


class Profile(ListView):
    models = User
    template_name = 'electronic_journal/profile.html'

    def get_queryset(self):
        return User.objects.get(slug=self.request.user.slug)

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_data'] = self.get_queryset()
        context['quests'] = Quest.objects.filter(group=self.request.user.group)[:5]
        context['userquests'] = UserQuest.objects.filter(user=self.request.user)
        return context


class QuestView(ListView):
    model = Quest
    template_name = 'electronic_journal/Quest.html'
    context_object_name = 'quests'


def logout_user(request):
    logout(request)
    return redirect('login')