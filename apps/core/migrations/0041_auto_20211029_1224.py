# Generated by Django 3.2.2 on 2021-10-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20210824_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='anketa',
            name='anketa_pometka_na_udalenie',
            field=models.BooleanField(default=False, verbose_name='Пометка на удаление'),
        ),
        migrations.AddField(
            model_name='beremennaya',
            name='beremennaya_pometka_na_udalenie',
            field=models.BooleanField(default=False, verbose_name='Пометка на удаление'),
        ),
        migrations.AddField(
            model_name='konsultaciaya',
            name='konsultaciya_pometka_na_udalenie',
            field=models.BooleanField(default=False, verbose_name='Пометка на удаление'),
        ),
        migrations.AddField(
            model_name='napravlenie',
            name='napravlenie_pometka_na_udalenie',
            field=models.BooleanField(default=False, verbose_name='Пометка на удаление'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='napravlena_na_extrennoe_rodorazreshenie',
            field=models.BooleanField(default=False, verbose_name='Направлена на экстренное родоразрешение'),
        ),
    ]
