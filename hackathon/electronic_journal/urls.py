from django.urls import path

from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('account/create/', UserRegistrationView.as_view(), name='signup'),
    path('profile/<int:user_id>', Profile.as_view(), name='profile'),
    path('quest', Quest.as_view(), name='quest'),
]
