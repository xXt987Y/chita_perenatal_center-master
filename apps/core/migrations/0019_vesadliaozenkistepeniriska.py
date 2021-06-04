# Generated by Django 3.2.2 on 2021-06-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210531_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='VesaDliaOzenkiStepeniRiska',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_gde_smotret', models.CharField(choices=[('Anketi', 'Анкеты'), ('Beremennaya', 'Беременная')], max_length=255, verbose_name='Модель где смотреть')),
                ('stolbez_gde_smotret', models.CharField(max_length=255, verbose_name='Столбец/поле где смотреть')),
                ('znachenie', models.CharField(help_text='Например: "True", "False", "1", "2"(id) . Без кавычек и с учетом регистра', max_length=255, verbose_name='Значение при оценки')),
                ('ozenka', models.IntegerField(default=0, verbose_name='Оценка при выбраном значение')),
            ],
            options={
                'verbose_name_plural': 'Веса для оценки степени риска',
            },
        ),
    ]
