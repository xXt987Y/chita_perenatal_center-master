# Generated by Django 3.2.2 on 2021-05-22 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210522_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='beremennaya',
            name='rubec_na_matke',
            field=models.BooleanField(default=False, verbose_name='рубец на матке после миомэктомии'),
        ),
    ]