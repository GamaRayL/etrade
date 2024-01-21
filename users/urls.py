from django.urls import path

from users.apps import UsersConfig
from users.views import UserRegistrationAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view(), name='register'),
]
