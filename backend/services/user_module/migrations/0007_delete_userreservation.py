# Generated by Django 4.1.1 on 2023-06-15 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0006_alter_useraddress_address_alter_useraddress_city_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserReservation',
        ),
    ]
