# Generated by Django 3.2.2 on 2021-07-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20210729_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polzovateli',
            name='rol',
            field=models.IntegerField(choices=[(1, 'админ края'), (2, 'админ ЖК'), (3, 'врач ЖК'), (4, 'консультант ЖК')], verbose_name='Роль'),
        ),
        migrations.DeleteModel(
            name='Roli',
        ),
    ]
