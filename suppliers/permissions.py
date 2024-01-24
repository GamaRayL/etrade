from rest_framework.permissions import BasePermission


class IsUserActive(BasePermission):
    """
    Проверка на активацию пользователя.
    Если он активирован, то допущен до API.
    """

    def has_permission(self, request, view):
        return request.user.is_active
