from django.db import models

from constants import NULLABLE


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=255, verbose_name='название')
    model = models.CharField(max_length=255, **NULLABLE, verbose_name='модель')
    release_date = models.DateField(**NULLABLE, verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name} - {self.model}. Релиз: {self.release_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
