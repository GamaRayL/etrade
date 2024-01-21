from rest_framework.generics import CreateAPIView

from users.models import User


class UserRegistrationAPIView(CreateAPIView):
    def perform_create(self, serializer):
        user = User.objects.create_user(
            email=serializer.validated_data('email'),
            password=serializer.validated_data('password')
        )
        user.save()

        return user
