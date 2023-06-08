from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models

from services.file_module.models import File

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'categories'
#
#     def __str__(self):
#         return self.name
#
# class TestTable(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Title')
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
#     def delete(self, *args, **kwargs):
#         super().delete(*args, **kwargs)


class Currency(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    symbol = models.CharField(max_length=1, verbose_name='Symbol')
    price = models.FloatField(verbose_name='Price')
    is_default = models.BooleanField(default=False, verbose_name='Default')

    def __str__(self):
        return self.title

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
    category = models.ManyToManyField(Category)
    # category = models.TextField(max_length=255, verbose_name='Category')
    currency = models.ForeignKey(Currency,
                                 on_delete=models.CASCADE,
                                 verbose_name='Currency',
                                 related_name='products')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', related_name='products')
    in_stock = models.BooleanField(default=True, verbose_name='In Stock')

    @property
    def owner_email(self):
        return self.owner.email

    @property
    def files(self):
        files = File.objects.filter(object_id=self.id,
                                    content_type_id=ContentType.objects.get_for_model(Product).id)
        if files.exists():
            return files[0].absolute_file_url
