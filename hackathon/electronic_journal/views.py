from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import LoginForm, UserRegistrationForm, CreateQuestForm
from .models import Quest, UserQuest, User
from .forms import LoginForm, UserRegistrationForm
from .models import Quest, UserQuest, User, EmailVerification


class Login(LoginView):
    form_class = LoginForm
    template_name = 'electronic_journal/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')  # указать профиль


def logout_user(request):
    logout(request)
    return redirect('login')


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
    model = Quest
    template_name = 'electronic_journal/Quest.html'
    context_object_name = 'quests'


class EmailVerificationView(TemplateView):
    template_name = 'electronic_journal/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.verification = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login'))
