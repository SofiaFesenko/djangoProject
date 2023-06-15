from django.contrib import admin

from services.products_module.filter import CurrencyFilter
from services.products_module.models import Currency, Product, Category


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    search_fields = ['id', 'title', 'symbol']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'owner_email', 'in_stock']
    search_fields = ['id', 'title', 'owner__email']
    list_filter = ('in_stock', CurrencyFilter)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title']

    def title(self, obj):
        return obj.description
