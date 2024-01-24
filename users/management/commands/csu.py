from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        email = 'admin@gmail.com'
        password = 'admin'

        user = User.objects.create_superuser(
            email=email,
            password=password,
        )
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f'Суперпользователь с почтой {email} успешно создан!')
        )
