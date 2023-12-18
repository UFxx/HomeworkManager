from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import LoginForm, UserRegistrationForm
from .models import User,  Quest, UserQuest


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


# class Profile(ListView):
#     models = User
#     template_name = 'electronic_journal/profile.html'
#
#     def get_queryset(self):
#         return User.objects.get(slug=self.request.user)
#
#     def get_context_data(self, object_list=None, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['user_data'] = self.get_queryset()
#         # context['quest'] = Quest.objects.filter(group=self.request.user.group)
#         context['userquest'] = UserQuest.object.filter(user=self.request.user)
#         return context