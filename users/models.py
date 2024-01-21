import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

from constants import MEMBER, USER_ROLES, ADMIN


class UserManager(BaseUserManager):
    """Менеджер под создание пользователя"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле "email" должно быть заполнено!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', MEMBER)
        extra_fields.setdefault('key', uuid.uuid4())
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', ADMIN)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None

    email = models.EmailField(max_length=255, verbose_name='почта')
    is_active = models.BooleanField(default=False, verbose_name='активен')
    key = models.CharField(max_length=100, verbose_name='ключ')
    role = models.CharField(max_length=20,
                            choices=USER_ROLES.items(),
                            default=MEMBER,
                            verbose_name='роль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
