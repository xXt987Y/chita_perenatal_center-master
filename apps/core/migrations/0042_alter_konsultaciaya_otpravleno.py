# Generated by Django 3.2.2 on 2021-11-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20211029_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konsultaciaya',
            name='otpravleno',
            field=models.DateField(auto_now=True, null=True, verbose_name='Отправлено (дата отправления)'),
        ),
    ]
