from django.db import models

from constants import NULLABLE
from contacts.models import Contact
from products.models import Product


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    contact = models.ForeignKey(Contact,
                                **NULLABLE,
                                on_delete=models.SET_NULL,
                                related_name='contact',
                                verbose_name='контакты')
    products = models.ManyToManyField(Product,
                                      **NULLABLE,
                                      related_name='products',
                                      verbose_name='продукты'
                                      )
    subpartner = models.ForeignKey('self',
                                   **NULLABLE,
                                   on_delete=models.SET_NULL,
                                   related_name='subpartner',
                                   verbose_name='поставщик'
                                   )
    debt = models.DecimalField(max_digits=50,
                               decimal_places=2,
                               default=0.0,
                               verbose_name='задолженность'
                               )
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
