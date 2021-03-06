# Generated by Django 3.2.2 on 2021-06-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20210613_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeet_socialnie_faktori',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет ли социальные факторы риска (курение, алкоголизм, наркомания)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_geneticheskih',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие генетических факторов (ВПР, наследственные заболевания)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='vzata_na_uchet',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Взята на учет после 12-ти недель беременности'),
        ),
    ]
