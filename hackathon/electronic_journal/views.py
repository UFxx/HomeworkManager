from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import LoginForm, UserRegistrationForm, CreateQuestForm
from .models import Quest, UserQuest, User

class Login(LoginView):
    form_class = LoginForm
    template_name = 'electronic_journal/login.html'

    def get_success_url(self):
        return reverse_lazy('login')  # указать профиль


class UserRegistrationView(CreateView):
    """Регистрация"""
    model = get_user_model()
    form_class = UserRegistrationForm
    template_name = 'electronic_journal/registration.html'

    def get_success_url(self):
        return reverse_lazy('login')


class Profile(LoginRequiredMixin, CreateView):
    models = User
    form_class = CreateQuestForm
    template_name = 'electronic_journal/profile.html'

    def get_queryset(self):
        return User.objects.prefetch_related('group').get(slug=self.request.user.slug)

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_data'] = self.get_queryset()
        context['quests'] = Quest.objects.filter(group=self.request.user.group).prefetch_related('teacher', 'subject')
        context['user_quests'] = UserQuest.objects.filter(user=self.request.user).prefetch_related('user', 'quest')
        return context

    def get_success_url(self):
        return reverse_lazy('profile')

# def post(self, request):
#     form = self.form_class(request.POST, request.FILES)
#     if form.is_valid():
#         # Обработка успешного запроса
#         print(form.data)
#         form.save()
#     else:
#         return render(request, self.template_name, {'form': form})

class QuestView(ListView):
    model = UserQuest
    template_name = 'electronic_journal/tasks.html'
