from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериалайзер для User(пользователя)"""

    class Meta:
        model = User
        fields = ('email', 'password')
