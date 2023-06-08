from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_seller = models.BooleanField(default=False, verbose_name='Seller')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # TODO додати створення налаштувань у методі save

    def save(self, *args, **kwargs):
        from services.products_module.models import Currency
        if not Currency.objects.exists():
            currency = Currency.objects.create(title='USD', symbol='$', price=0)
        else:
            currency = Currency.objects.first()
        super().save(*args, **kwargs)
        UserSettings.objects.get_or_create(user=self, currency=currency)


class UserAddress(models.Model):
    country = models.CharField(max_length=255, verbose_name='Country')
    city = models.CharField(max_length=255, verbose_name='City')
    address = models.CharField(max_length=255, verbose_name='Address')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_address')


class UserSettings(models.Model):
    currency = models.ForeignKey('products_module.Currency',
                                 on_delete=models.CASCADE,
                                 verbose_name='Currency',
                                 related_name='user_settings')
    is_send_push = models.BooleanField(default=True, verbose_name='Send Push')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_settings')


class UserReservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    people_choices = ((one, 'one person'), (two, 'two people'), (three, 'three people'),
                      (four, 'four people'), (five, 'five  people'))
    people = models.CharField(max_length=1, choices=people_choices, default=one)
    date = models.DateField()
    time = models.TimeField()
    # pending = "pending"
    # confirmed = "confirmed"
    # status_choices = ((pending, "pending"), (confirmed, "confirmed"))
    # status = models.CharField(
    #     max_length=10, choices=status_choices, default=pending)
    # comment = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
