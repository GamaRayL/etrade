from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Добавление Supplier(поставщика) в админ панель.
    Также здесь добавлена ссылка(supplier_link) на поставщика и
    действие(clear_debt) очистки задолженности.
    """
    list_display = ('name', 'email', 'country',
                    'city', 'street', 'house_number',
                    'supplier_link', 'debt',)
    list_filter = ('city',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            app_label = obj._meta.app_label
            model_label = obj._meta.model_name
            url = reverse(
                f'admin:{app_label}_{model_label}_change', args=(obj.supplier.id,)
            )
            return mark_safe(f'<a href="{url}">{obj.supplier.name}</a>')

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Ссылка на поставщика'

    def clear_debt(modelname, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"
