# Generated by Django 3.2.2 on 2021-05-15 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_smena_jk_u_beremennoy_nomer_beremennoy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medorganizacia',
            name='tip_organizacii',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, to='core.tiporganizacii', verbose_name='Тип организации'),
        ),
        migrations.AlterField(
            model_name='medorganizacia',
            name='uroven_med_obclujivaniya',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.urovenmedobsluzivaniya', verbose_name='Уровень медецинского обслуживания'),
        ),
    ]
