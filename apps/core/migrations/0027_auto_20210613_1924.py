# Generated by Django 3.2.2 on 2021-06-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_konsultaciaya_kontakt_s_socialno_tuberkulez'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konsultaciaya',
            name='IMT_bolee_35',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='ИМТ более 35'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='dva_i_bolee_med',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Два и более мед абортов'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='hirurgicheskie_vmeshatelstva',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет ли место хирургические вмешательства во время данной беременности'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='hirurgicheskoe_lechenie',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Хирургическое лечение шейки матки'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeet_mesto_krovotecheniya',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имели ли место кровотечения во время беременности'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeet_mesto_risk_razvitie',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет место риск развития проэклампсии (определяет консультант)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeet_mesto_risk_razvitiya',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет место риск развития гестационного сахарного диабета'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeet_risk_VPR',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет место риск ВПР'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeet_risk_po_razvitiy_GBN',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет место риск по развитию ГБН'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeet_socialnie_faktori',
            field=models.IntegerField(blank=True, default=False, null=True, verbose_name='Имеет ли социальные факторы риска (курение, алкоголизм, наркомания)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='imeli_matochnie',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имели ли место маточные кровотечения'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='infekcii_moche',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие инфекции моче-выводящих путей'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='kontakt_s_socialno',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Контакт с социально значимыми заболеваниями'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='kontakt_s_socialno_tuberkulez',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], null=True, verbose_name='Туберкулез'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='kontakt_s_socialno_vich',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='ВИЧ'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='megdu_beremennostyami_10',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Интервал между беременностями более 10 лет'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='mesto_rojdeniya_v_anameze',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имело место рождения в анамезе крупных плодов (более 4,5 кг)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='mnogoplodnaya',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Многоплодная/индуциованная беременность'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_IMT',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие ИМТ'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_IPP',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие ИПП'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_alko',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие алкогольной/никотиновой зависимости'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_auto_imunnih',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие ауто-имунных заболеваний'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_geneticheskih',
            field=models.IntegerField(blank=True, default=False, null=True, verbose_name='Наличие генетических факторов (ВПР, наследственные заболевания)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_geneticheskoy_predraspol',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет место наличие генетической предрасположенности к сахарному диабету'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_hronicheskoy',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие хронической гипертензии'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_markerov',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие маркеров генетических заболеваний в биохимическом скрининге (PAPP-A, бетта-ХГЧ)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_nasledstvennih',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие наследственных тромбофилий'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_saharnogo',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие сахорного диабета 1 или 2 типа'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_tajoloy_patologii',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие тяжелой экстрагенитальной патологии'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_v_anameze',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие в анамезе проэклампсии'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='nalichie_v_anameze_34',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Наличие в анамезе проэклампсии преждевременных родов в сроке менее 34 недель'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='odin_i_bolee_vikidish',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Один и более выкидышей в анамнезе'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='odni_i_bolee_prej',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Один и более преждевременных родов в анамнезе'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='pervoberemennaya',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Первобеременная'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='predlejanie_placenti',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Предлежание плаценты'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='provedeno_uzi_12_14',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Проведено ли УЗИ на сроке 12-14 недель'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='provodilos_lechebnie',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Проводились лечебные и диагностические мероприятия (биопсия хориона, амнионтез, кордоцентез, серкляж)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='provodilos_perelivanie',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Проводилось ли переливание крови без учета резус принадлежности женщинам с резус-отрицательно кровью'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='risk_prejdevremennih_rodov',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет место риск преждевременных родов (определяет консультант)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='soprovagdalas_predidushaya',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Сопровождалась предыдущая беременность гестационным сахарным диабетом'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='v_rezultate_ECO',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Имеет беременность в результате ЭКО'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='visokiy_paritet',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Высокий паритет (более 4 родов)'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='vozrast_18_34',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Возраст менее 18 или более 34 лет'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='vozrast_bolee_40',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Возраст более 40 лет'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='vzata_na_uchet',
            field=models.IntegerField(blank=True, default=False, null=True, verbose_name='Взята на учет после 12-ти недель беременности'),
        ),
        migrations.AlterField(
            model_name='konsultaciaya',
            name='zanesena_v_monitoring',
            field=models.IntegerField(blank=True, choices=[(None, 'Неизвестно'), (0, 'Нет'), (1, 'Да')], default=False, null=True, verbose_name='Занесена в мониторинг беременных'),
        ),
    ]
