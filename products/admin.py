from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Регистрация Product(продукта) в админ панели.
    Также добававлено новое поле "display_suppliers",
    который отображает у каких поставщиков добавлен этот товар.
    """
    list_display = ('name', 'model', 'release_date', 'display_suppliers',)

    def display_suppliers(self, obj):
        return ", ".join([supplier.name for supplier in obj.products.all()])

    display_suppliers.short_description = 'Числится'
