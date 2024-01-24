from django.db import models

from constants import NULLABLE
from products.models import Product


class Supplier(models.Model):
    """Поставщик или звено"""
    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(max_length=255, verbose_name='почта')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=255, verbose_name='номер дома')
    products = models.ManyToManyField(Product, related_name='products',
                                      verbose_name='продукты')
    supplier = models.ForeignKey('self',
                                 **NULLABLE,
                                 on_delete=models.SET_NULL,
                                 related_name='subsupplier',
                                 verbose_name='поставщик'
                                 )
    debt = models.DecimalField(max_digits=50,
                               decimal_places=2,
                               default=0.0,
                               verbose_name='задолженность'
                               )
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    class Meta:
        verbose_name = 'поставщика'
        verbose_name_plural = 'поставщики'

    def __str__(self):
        return self.name
