import django_filters
from django.contrib import admin

from services.products_module.models import Product, Currency


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    owner__username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['price', 'in_stock', 'owner']


class CurrencyFilter(admin.SimpleListFilter):
    title = 'currency_filter'
    parameter_name = 'currency_filter'

    def lookups(self, request, model_admin):
        currency = [(currency.id, currency.title) for currency in Currency.objects.all()]
        return tuple(currency)

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(currency_id=value)
        return queryset


# class CategoryFilter(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = 'category'

# class CategoryFilter():
#     pass
