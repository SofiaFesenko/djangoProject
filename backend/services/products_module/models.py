from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Currency(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    symbol = models.CharField(max_length=1, verbose_name='Symbol')
    price = models.FloatField(verbose_name='Price')
    is_default = models.BooleanField(default=False, verbose_name='Default')

    def save(self, *args, **kwargs):
        if not self.is_default:
            if not Currency.objects.filter(is_default=True).exists():
                self.is_default = True
        else:
            Currency.objects.filter(is_default=True).update(is_default=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if self.is_default:
            currency = Currency.objects.first()
            if currency:
                currency.is_default=True
                currency.save()


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(max_length=2000, verbose_name='Description')
    price = models.FloatField(verbose_name='Price')
    currency = models.ForeignKey(Currency,
                                 on_delete=models.CASCADE,
                                 verbose_name='Currency',
                                 related_name='products')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', related_name='products')
    in_stock = models.BooleanField(default=True, verbose_name='In Stock')
