# Generated by Django 3.2.2 on 2021-06-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_konsultaciaya_kontakt_s_socialno_tuberkulez'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konsultaciaya',
            name='kontakt_s_socialno_tuberkulez',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (True, 'Да'), (False, 'Нет')], null=True, verbose_name='Туберкулез'),
        ),
    ]