from django.urls import path

from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('account/create/', UserRegistrationView.as_view(), name='signup'),
    path('profile', Profile.as_view(), name='profile'),

]
