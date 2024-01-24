# Generated by Django 5.0.1 on 2024-01-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0002_alter_supplier_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='products',
            field=models.ManyToManyField(related_name='products', to='products.product', verbose_name='продукты'),
        ),
    ]