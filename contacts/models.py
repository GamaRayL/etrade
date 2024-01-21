from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=255, verbose_name='почта')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=255, verbose_name='номер дома')

    def __str__(self):
        return f'Контакт с ID {self.pk} ({self.email})'
