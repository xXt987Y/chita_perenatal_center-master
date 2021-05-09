# Generated by Django 3.2 on 2021-05-05 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210505_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='novorojdenniy',
            name='prichina_smerti_materi_po_mkb10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smerti_novorojdennogo', to='core.mkb10', verbose_name='Причина смерти матери по МКБ-10'),
        ),
        migrations.AlterField(
            model_name='autorecomendacii',
            name='vozrastnaya_grupa',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Возрастная группа/диагноз'),
        ),
    ]
