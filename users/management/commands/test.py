from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = 'admin@gmail.com'
        password = 'admin'
        
        try:
            user = User.objects.create_user(
                email=email,
                password=password,
                is_active=True
            )
            user.save()

            self.stdout.write(
                self.style.SUCCESS(f'Суперпользователь с почтой {email} успешно создан!')
            )

        except KeyboardInterrupt:
            self.stdout.write(
                self.style.WARNING("\nПрограмма была прервана пользователем.")
            )
