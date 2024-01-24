from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Добавление User(пользователя) в админ панель"""
    list_display = ('email', 'role', 'is_active',)
