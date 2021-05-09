from django.contrib.auth.models import User
from django.db import models

UROVEN_MO = ((1, '1'),
             (2, '2'),
             (3, '3'))
TIP_ORGANIZACII = ((1, 'Женская консультация'),
                   (2, 'Род.дом'),
                   (3, 'Консультация'))
REZUS_FAKTORI = ((1, '+/+'),
                 (2, '+/-'),
                 (3, '-/+'),
                 (4, '-/-'))

POL = ((1, 'М'),
       (2, 'Ж'),
       (3, 'Неизвестен'),
       (4, 'Интерсекс'))


class Rayon(models.Model):
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)
    korotkoe_nazvanie = models.CharField(verbose_name='Короткое название', max_length=255)
    v_chite = models.BooleanField('Находится в Чите?Да/Нет', default=False, blank=True)

    def __str__(self):
        return self.nazvanie


# class idMedOrg(models.Model):
#     class Meta:
#         verbose_name_plural = 'ID Медицинская организация'
#         verbose_name_plural = 'ID Медицинские организации'
#
#     nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True)
#
class UrovenMedObsluzivaniya(models.Model):
    class Meta:
        verbose_name = 'Уровень медецинского обслуживания'
        verbose_name_plural = 'Уровень медецинского обслуживания'

    nazvanie = models.CharField(verbose_name='Уровень мед обслуживания', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class TipOrganizacii(models.Model):
    class Meta:
        verbose_name = 'Тип организации'
        verbose_name_plural = 'Тип организации'

    nazvanie = models.CharField(verbose_name='Тип мед организации', max_length=255, null=True, blank=True)

    # Консультация, роддом, женская консультация
    def __str__(self):
        return self.nazvanie


class MedOrganizacia(models.Model):
    class Meta:
        verbose_name = 'Медицинская организация'
        verbose_name_plural = 'Медицинские организации'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)
    rayon = models.ForeignKey(Rayon, verbose_name='Район', on_delete=models.CASCADE, null=True, blank=True)
    tip_organizacii = models.ForeignKey(TipOrganizacii, on_delete=models.CASCADE, default=True, blank=True)
    uroven_med_obclujivaniya = models.ForeignKey(UrovenMedObsluzivaniya, on_delete=models.CASCADE, null=True,
                                                 blank=True)
    ZKPC = models.BooleanField('ЗКПЦ? Да/Нет', default=True, blank=True)
    email = models.CharField(verbose_name='Электронная почта', max_length=255, null=True, blank=True)
    kontaktnaya_informaciya = models.TextField('Контактная информация', null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Roli(models.Model):
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    nazvanie = models.CharField(verbose_name='Название роли', max_length=255, null=True, blank=True)

    # Оператор женской консультации, Оператор Род Дома
    def __str__(self):
        return self.nazvanie


class Polzovateli(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user = models.OneToOneField(User, verbose_name='Юзер', on_delete=models.CASCADE)
    med_organiizaciya = models.ForeignKey(MedOrganizacia, verbose_name='Медицинская организация',
                                          on_delete=models.CASCADE, null=True, blank=True)
    # выпадающие списки из таблицы роли
    rol = models.ForeignKey(Roli, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.rol.nazvanie}'


class Doctor(models.Model):
    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    med_organiizaciya = models.ForeignKey(MedOrganizacia, verbose_name='Медицинская организация',
                                          on_delete=models.CASCADE, null=True, blank=True)
    fio = models.CharField(verbose_name='ФИО', max_length=255, null=True, blank=True)
    rabotaet = models.BooleanField('Работает?Да/Нет', default=True, blank=True)

    def __str__(self):
        return self.fio


class MKB10(models.Model):
    class Meta:
        verbose_name = 'Код по МКБ10'
        verbose_name_plural = 'Коды по МКБ10'

    kod = models.CharField(verbose_name='Код по МКБ10', max_length=255, null=True, blank=True)
    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Autorecomendacii(models.Model):
    class Meta:
        verbose_name = 'Авторекомендация'
        verbose_name_plural = 'Авторекомендации'

    code = models.CharField('Код авторекомендации', max_length=255, null=True, blank=True)
    vozrastnaya_grupa = models.CharField(verbose_name='Возрастная группа/диагноз', max_length=255, null=True,
                                         blank=True)
    recomendaciya = models.TextField('Текст рекомендации', null=True, blank=True)
    use = models.BooleanField('Использовать', default=False)

    def __str__(self):
        return self.vozrastnaya_grupa


class StepenRiska(models.Model):
    class Meta:
        verbose_name = 'Степень риска'
        verbose_name_plural = 'Степени риска'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class SemeynoePolojenie(models.Model):
    class Meta:
        verbose_name = 'Семейное положение'
        verbose_name_plural = 'Семейное положение'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class GeneticheskieFaktori(models.Model):
    class Meta:
        verbose_name = 'Генетический фактор'
        verbose_name_plural = 'Генетические факторы'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class MenstrualnayaFunkciya(models.Model):
    class Meta:
        verbose_name = 'Менструальная функция'
        verbose_name_plural = 'Менструальная функции'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Besplodie(models.Model):
    class Meta:
        verbose_name = 'Бесплодие'
        verbose_name_plural = 'Бесплодие'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class TipBesplodiya(models.Model):
    class Meta:
        verbose_name = 'Тип бесплодия'
        verbose_name_plural = 'Типы бесплодия'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class NastuplenieBeremennostiVRezultate(models.Model):
    class Meta:
        verbose_name = 'Наступление беременности в результате ЭКО'
        verbose_name_plural = 'Наступление беременности в результате ЭКО'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class ParitetBeremennosti(models.Model):
    class Meta:
        verbose_name = 'Паритет беременности'
        verbose_name_plural = 'Паритет беременности'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class SamoproizvolniyAbort(models.Model):
    class Meta:
        verbose_name = 'Самопроизвольный аборт'
        verbose_name_plural = 'Самопроизвольный аборт'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class IskustvenniyAbort(models.Model):
    class Meta:
        verbose_name = 'Искусственный аборт'
        verbose_name_plural = 'Искусственный аборт'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class OslojneniyaIskustvenniyAbort(models.Model):
    class Meta:
        verbose_name = 'Осложнения'
        verbose_name_plural = 'Осложнения'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class OslojneniyaBeremennostiAnamez(models.Model):
    class Meta:
        verbose_name = 'Осложнения беременности (анамез)'
        verbose_name_plural = 'Осложнения беременности (анамез)'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class KesarevoSechenie(models.Model):
    class Meta:
        verbose_name = 'Кесарево сечение для анкеты беременной'
        verbose_name_plural = 'Кесарево сечение для анкеты беременной'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class SaharniyDiabed(models.Model):
    class Meta:
        verbose_name = 'Сахарный диабет'
        verbose_name_plural = 'Сахарный диабет'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class GestacionniySaharniyDiabed(models.Model):
    class Meta:
        verbose_name = 'Гестационный сахарный диабет'
        verbose_name_plural = 'Гестационный сахарный диабет'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class ZabolevanieShitovidnoy(models.Model):
    class Meta:
        verbose_name = 'Заболевание щитовидной железы'
        verbose_name_plural = 'Заболевания щитовидной железы'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class AKO(models.Model):
    class Meta:
        verbose_name = 'АКО'
        verbose_name_plural = 'АКО'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Koagulopatiya(models.Model):
    class Meta:
        verbose_name = 'Коагулопатия'
        verbose_name_plural = 'Коагулопатия'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class FormaSujeniyaTaza(models.Model):
    class Meta:
        verbose_name = 'Форма сужения таза'
        verbose_name_plural = 'Форма сужения таза'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class StepenSujeniyaTaza(models.Model):
    class Meta:
        verbose_name = 'Степень сужения таза'
        verbose_name_plural = 'Степень сужения таза'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class VzyataPodNabludenie(models.Model):
    class Meta:
        verbose_name = 'Взята под наблюдение'
        verbose_name_plural = 'Взята под наблюдение'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class OslojneniyaRodov(models.Model):
    class Meta:
        verbose_name = 'Осложнения родов'
        verbose_name_plural = 'Осложнения родов'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Beremennaya(models.Model):
    class Meta:
        verbose_name = 'Беременная'
        verbose_name_plural = 'Беременные'

    nomer = models.CharField('Номер', max_length=255, null=True, blank=True, unique=True)
    stepen_riska = models.ForeignKey(StepenRiska, verbose_name='Степень риска', on_delete=models.CASCADE, null=True,
                                     blank=True)
    data_vzyatiya = models.DateField('Дата взятия', null=True, blank=True)
    vrach = models.ForeignKey(Doctor, verbose_name='Врач', on_delete=models.CASCADE, null=True,
                              blank=True)
    fio = models.CharField('ФИО беременной', max_length=255, null=True, blank=True)
    data_rojdeniya = models.DateField('Дата рождения', null=True, blank=True)
    vozrast = models.CharField('Возраст беременной', max_length=255, null=True, blank=True)
    mesto_postoyannogo_projivaniya = models.ForeignKey(Rayon, verbose_name='Место постоянного проживания',
                                                       on_delete=models.CASCADE, null=True,
                                                       blank=True)
    nomer_telefona = models.CharField('Номер телефона', max_length=255, null=True, blank=True)
    nomer_oms = models.CharField('Номер ОМС беременной', max_length=255, null=True, blank=True)
    vrednie_privichki_kurenie = models.BooleanField('Курение', default=False)
    vrednie_privichki_alco = models.BooleanField('Алкоголизм', default=False)
    vrednie_privichki_narko = models.BooleanField('Наркомания', default=False)
    vrednie_privichki_toxi = models.BooleanField('Таксикомания', default=False)
    vrednie_factori_truda_himicheskie = models.BooleanField('Химические', default=False)
    vrednie_factori_truda_radioactiv = models.BooleanField('Радиоактивные', default=False)
    vrednie_factori_truda_priem_lekarstvennih_sredstv = models.BooleanField(
        'Прием лек. средств в ранние сроки беременности', default=False)
    vrednie_factori_truda_neudvl_jil_ysloviya = models.BooleanField('Неудвл. жил. условия', default=False)
    socialno_ugrojaemaya = models.BooleanField('Социально угрожаемая', default=False)
    semeynoe_polojenie = models.ForeignKey(SemeynoePolojenie, verbose_name='Семейное положение',
                                           on_delete=models.CASCADE, null=True,
                                           blank=True)
    somaticheskie_pokazateli_muzskoy = models.BooleanField('Мужской тип телосложения', default=False)
    somaticheskie_pokazateli_girsutizm = models.BooleanField('Гирсутизм', default=False)
    ves = models.CharField('Вес беременной', max_length=255, null=True, blank=True)
    rost = models.CharField('Рост беременной', max_length=255, null=True, blank=True)
    index = models.CharField('Индекс массы тела', max_length=255, null=True, blank=True)
    razmer_taza_ds = models.CharField('Distania spinarium', max_length=255, null=True, blank=True)
    razmer_taza_dc = models.CharField('Distania cristarum', max_length=255, null=True, blank=True)
    razmer_taza_dt = models.CharField('Distania trochanterica', max_length=255, null=True, blank=True)
    razmer_taza_cd = models.CharField('Conjugata diagonalis', max_length=255, null=True, blank=True)
    razmer_taza_ce = models.CharField('Conjugata externa', max_length=255, null=True, blank=True)
    razmer_taza_cv = models.CharField('Conjugata vera', max_length=255, null=True, blank=True)
    forma_sujeniya_taza = models.ForeignKey(FormaSujeniyaTaza, verbose_name='Форма сужения таза',
                                            on_delete=models.CASCADE, null=True,
                                            blank=True)
    stepen_sujeniya_taza = models.ForeignKey(StepenSujeniyaTaza, verbose_name='Степень сужения таза',
                                             on_delete=models.CASCADE, null=True,
                                             blank=True)
    rezus_faktori_beremennoy_otca = models.IntegerField('Резус факторы беременной/отца', choices=REZUS_FAKTORI,
                                                        null=True, blank=True)
    vzyata_pod_nabludenie = models.ForeignKey(VzyataPodNabludenie, verbose_name='Взята под наблюдение',
                                              on_delete=models.CASCADE, null=True,
                                              blank=True)
    geneticheskie_faktori = models.ForeignKey(GeneticheskieFaktori, verbose_name='Генетические факторы',
                                              on_delete=models.CASCADE, null=True,
                                              blank=True)
    menstrualnaya_funkciya = models.ForeignKey(MenstrualnayaFunkciya, verbose_name='Менструальная функция',
                                               on_delete=models.CASCADE, null=True,
                                               blank=True)
    zabolevanie_vnut_pol_organov_vospalenie_neroj = models.BooleanField('Воспаление придатков у нерожавшей',
                                                                        default=False)
    zabolevanie_vnut_pol_organov_vospalenie_roj = models.BooleanField('Воспаление придатков у рожавшей', default=False)
    zabolevanie_vnut_pol_organov_opuhl = models.BooleanField('Опухлевое образование придатков', default=False)
    zabolevanie_vnut_pol_organov_mioma = models.BooleanField('Миома матки', default=False)
    zabolevanie_vnut_pol_organov_gipoplaziya = models.BooleanField('Гипоплазия матки', default=False)
    zabolevanie_vnut_pol_organov_poroki = models.BooleanField('Пороки развития матки', default=False)
    zabolevanie_vnut_pol_organov_operacii_pred = models.BooleanField('Операции на придатках', default=False)
    zabolevanie_vnut_pol_organov_operacii_matk = models.BooleanField('Операции на матке (кроме кес/сеч)', default=False)
    zabolevanie_vnut_pol_organov_istmiko = models.BooleanField('Истмико-цервикальная недостаточность', default=False)
    zabolevanie_vnut_pol_organov_onkologiya = models.BooleanField('Онкология в анамезе', default=False)
    besplodie = models.ForeignKey(Besplodie, verbose_name='Бесплодие',
                                  on_delete=models.CASCADE, null=True,
                                  blank=True)
    tip_besplodiya = models.ForeignKey(TipBesplodiya, verbose_name='Тип бесплодия',
                                       on_delete=models.CASCADE, null=True,
                                       blank=True)
    nastuplenie_beremennosti_v_rezultate_eco = models.ForeignKey(NastuplenieBeremennostiVRezultate,
                                                                 verbose_name='Наступление беременности в результате ЭКО',
                                                                 on_delete=models.CASCADE, null=True,
                                                                 blank=True)
    nastuplenie_beremennosti_v_rezultate_ovulyacii = models.BooleanField(
        'Наступление беременности в результате стимуляции овуляции медикаментозными средствами', default=False)
    data_pervogo_dnya_posledney_menstruacii = models.DateField('Дата первого дня последней менструации', null=True,
                                                               blank=True)
    paritet_beremennosti = models.ForeignKey(ParitetBeremennosti, verbose_name='Паритет беременности',
                                             on_delete=models.CASCADE, null=True,
                                             blank=True)
    samoproizvolniy_abort = models.ForeignKey(SamoproizvolniyAbort, verbose_name='Самопроизвольный аборт',
                                              on_delete=models.CASCADE, null=True,
                                              blank=True)
    vnematochnaya_beremennost = models.BooleanField('Внематочная беременность', default=False)
    rezus_konfliktnaya_beremennost = models.BooleanField('Резус-конфликтная беременность', default=False)
    gemoliticheskaya_bolezn = models.BooleanField('Гемолитическая болезнь плода или новорожденного', default=False)
    iskustvenniy_abort = models.ForeignKey(IskustvenniyAbort, verbose_name='Искусственный аборт',
                                           on_delete=models.CASCADE, null=True,
                                           blank=True)
    iskustvenniy_abort_oslojneniya = models.ForeignKey(OslojneniyaIskustvenniyAbort, verbose_name='Осложнения',
                                                       on_delete=models.CASCADE, null=True,
                                                       blank=True)
    oslojneniya_beremennosti_anemez = models.ForeignKey(OslojneniyaBeremennostiAnamez,
                                                        verbose_name='Осложнение беременности (анамез)',
                                                        on_delete=models.CASCADE, null=True,
                                                        blank=True)
    oslojneniya_beremennosti_anemez_fetoplacent = models.BooleanField('Осложн. фетоплацент. недостаточностью',
                                                                      default=False)
    oslojneniya_beremennosti_anemez_obostrenie = models.BooleanField('Осложн. обостр. экстрагенит. патологии',
                                                                     default=False)
    oslojneniya_beremennosti_anemez_prejdevremennoy = models.BooleanField('Осложн. преждевремен. отслойкой плаценты',
                                                                          default=False)
    oslojneniya_rodov = models.ForeignKey(OslojneniyaRodov, verbose_name='Осложнения родов',
                                          on_delete=models.CASCADE, null=True,
                                          blank=True)
    oslojneniya_rodov_osl_razrivom = models.BooleanField('Ослож. разрывом мягких родовых путей 2-3 степени',
                                                         default=False)
    oslojneniya_rodov_osl_krovotech = models.BooleanField('Ослож. кровотечением', default=False)
    oslojneniya_rodov_osl_gnoyno = models.BooleanField('Ослож. гнойно-септической инфекцией', default=False)
    oslojneniya_rodov_osl_mertvoroj = models.BooleanField('Ослож. мертворождением', default=False)
    kesarevo_sechenie = models.ForeignKey(KesarevoSechenie, verbose_name='Кесарево сечение',
                                          on_delete=models.CASCADE, null=True,
                                          blank=True)
    oslojneniya_anomaliyami_rodovoy_deyatelnosti = models.BooleanField('Ослож. аномалиями родовой деятельности',
                                                                       default=False)
    klinicheski_uzkiy_taz = models.BooleanField('Клинически узкий таз', default=False)
    plodorazrushayushaya_operaciya = models.BooleanField('Плодоразрушающая операция', default=False)
    novorojdenniy_plod_smert = models.BooleanField('Смерть в неонатальном периоде', default=False)
    novorojdenniy_plod_ves = models.BooleanField('Вес новорожденного был менее 2500г или более 4000г', default=False)
    novorojdenniy_plod_nevrolgiych = models.BooleanField('Неврологические нарушения', default=False)
    novorojdenniy_plod_vpr = models.BooleanField('ВПР', default=False)
    novorojdenniy_plod_perinatalnie = models.BooleanField('Перинатальные потери', default=False)
    infekcionnie_bolezni_gripp = models.BooleanField('Грипп', default=False)
    infekcionnie_bolezni_sifilis = models.BooleanField('Сифилис', default=False)
    infekcionnie_bolezni_vich = models.BooleanField('ВИЧ-инфекция', default=False)
    infekcionnie_bolezni_krasnuha = models.BooleanField('Краснуха', default=False)
    infekcionnie_bolezni_orvi = models.BooleanField('ОРВИ', default=False)
    infekcionnie_bolezni_tuberkulez = models.BooleanField('Туберкулез', default=False)
    infekcionnie_bolezni_virusniy_gepatit = models.BooleanField('Вирусный гепатит', default=False)
    zlokachestvennie_obrazovaniya = models.BooleanField('Наличие в прошлом и настоящем', default=False)
    saharniy_diabed = models.ForeignKey(SaharniyDiabed, verbose_name='Сахарный диабед',
                                        on_delete=models.CASCADE, null=True,
                                        blank=True)
    gestacionniy_saharniy_diabed = models.ForeignKey(GestacionniySaharniyDiabed,
                                                     verbose_name='Гестационный cахарный диабед',
                                                     on_delete=models.CASCADE, null=True,
                                                     blank=True)
    zabolevanie_shitovidnoy = models.ForeignKey(ZabolevanieShitovidnoy, verbose_name='Заболевание щитовидной железы',
                                                on_delete=models.CASCADE, null=True,
                                                blank=True)
    ako = models.ForeignKey(AKO, verbose_name='АКО',
                            on_delete=models.CASCADE, null=True,
                            blank=True)
    deincifalniy_sindrom = models.BooleanField('Диэнцефальный синдром', default=False)
    bolezni_krovi_anemiya = models.BooleanField('Анемия всех степеней', default=False)
    bolezni_krovi_trombocitopeniya = models.BooleanField('Тромбоцитопения', default=False)
    bolezni_krovi_trombozi = models.BooleanField('Тромбозы', default=False)
    koagulopatiya = models.ForeignKey(Koagulopatiya, verbose_name='Коагулопатия',
                                      on_delete=models.CASCADE, null=True,
                                      blank=True)
    psih_rastroystva_psihozi = models.BooleanField('Психозы', default=False)
    psih_rastroystva_narusheniya_lich = models.BooleanField('Нарушения личности', default=False)
    psih_rastroystva_shizofreniya = models.BooleanField('Шизофрения', default=False)
    psih_rastroystva_umstvennaya_otstalost = models.BooleanField('Умственная отсталость', default=False)
    bolezni_nervnoy_sistemi_nasledstvennie = models.BooleanField('Наследственные и дегенеративные болезни ЦНС',
                                                                 default=False)
    bolezni_nervnoy_sistemi_vospalitelnie = models.BooleanField('Воспалительные болезни ЦНС', default=False)
    bolezni_nervnoy_sistemi_miopiya = models.BooleanField(
        'Миопия высокой степени и миопия с дистрофическими изменениями', default=False)

    def __str__(self):
        return self.nomer


class Preeklampsiya(models.Model):
    class Meta:
        verbose_name = 'Преэклампсия'
        verbose_name_plural = 'Преэклампсия'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class RezusSensibilizaciya(models.Model):
    class Meta:
        verbose_name = 'Резус сенсибилизация'
        verbose_name_plural = 'Резус сенсибилизация'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class FetoplacentarnayaNedostatochnost(models.Model):
    class Meta:
        verbose_name = 'фетоплацентарная недостаточность'
        verbose_name_plural = 'фетоплацентарная недостаточность'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class NepravilnoePolojeniePloda(models.Model):
    class Meta:
        verbose_name = 'Неправильное положение плода'
        verbose_name_plural = 'Неправильное положение плода'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Mnogoplodie(models.Model):
    class Meta:
        verbose_name = 'Многоплодие'
        verbose_name_plural = 'Многоплодие'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class PredlejaniePlacenti(models.Model):
    class Meta:
        verbose_name = 'Предлежание плаценты'
        verbose_name_plural = 'Предлежание плаценты'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class UrovenPappa(models.Model):
    class Meta:
        verbose_name = 'Уровень РРАР-А'
        verbose_name_plural = 'Уровень РРАР-А'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class UrovenBetaHgch(models.Model):
    class Meta:
        verbose_name = 'Уровень бета ХГЧ'
        verbose_name_plural = 'Уровень бета ХГЧ'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class NalichieVprPoRezultatamUzi(models.Model):
    class Meta:
        verbose_name = 'Наличие ВПР по результатам УЗИ'
        verbose_name_plural = 'Наличие ВПР по результатам УЗИ'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class ObsheeSostoyaniePloda(models.Model):
    class Meta:
        verbose_name = 'Общее состояние плода'
        verbose_name_plural = 'Общее состояние плода'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Anketa(models.Model):
    class Meta:
        verbose_name = 'Анкета беременной'
        verbose_name_plural = 'Анкета беременной'

    nomer_anketi = models.ForeignKey(Beremennaya, verbose_name='Номер анкеты',
                                     on_delete=models.CASCADE, null=True,
                                     blank=True)
    data_zapolneniya_anketi_vrachem = models.DateField('Дата заполнения анкеты врачем', null=True, blank=True)
    familiya_vracha = models.ForeignKey(Doctor, verbose_name='Фамилия врача заполнившего анкету',
                                        on_delete=models.CASCADE, null=True,
                                        blank=True)
    ves_beremennoy = models.CharField('Вес беременной', max_length=255, null=True, blank=True)
    srok_beremennosti_po_obektivnim_dannim = models.CharField('По объективным данным', max_length=255, null=True,
                                                              blank=True)
    srok_beremennosti_po_dannim_uzi = models.CharField('По данным УЗИ', max_length=255, null=True, blank=True)
    srok_beremennosti_po_pervomu = models.CharField('По первому шевелению плода', max_length=255, null=True, blank=True)
    osobennosti_protekaniya_beremennosti_krovynistie = models.BooleanField(
        'Кровянистые выделения в дни, соответств. ожидаемой менструации', default=False)
    osobennosti_protekaniya_beremennosti_virazenniy_toxikoz = models.BooleanField(
        'Выраженный токсикоз ', default=False)
    osobennosti_protekaniya_beremennosti_krovotechenie = models.BooleanField(
        'Кровотечение', default=False)
    ugroza_prerivaniya_do_22 = models.BooleanField('До 22-ти недельного срока', default=False)
    ugroza_prerivaniya_posle_22 = models.BooleanField('После 22-ти недельного срока', default=False)
    antifosfolipidniy_sindrom = models.BooleanField('Есть', default=False)
    preeklampsiya = models.ForeignKey(Preeklampsiya, verbose_name='Преэклампсия',
                                      on_delete=models.CASCADE, null=True,
                                      blank=True)
    rezus_sensibilizaciya = models.ForeignKey(RezusSensibilizaciya, verbose_name='Резус-сенсибилизация',
                                              on_delete=models.CASCADE, null=True,
                                              blank=True)
    abo_sensibilizaciya = models.BooleanField('ABO-сенсибилизация', default=False)
    fetoplacentarnaya_nedostatochnost = models.ForeignKey(FetoplacentarnayaNedostatochnost,
                                                          verbose_name='Фетоплацентарная недостаточность',
                                                          on_delete=models.CASCADE, null=True,
                                                          blank=True)
    narushenie_okoplodnih_vod_mnogovodie = models.BooleanField('Многоводие', default=False)
    narushenie_okoplodnih_vod_malovodie = models.BooleanField('Маловодие', default=False)
    narushenie_okoplodnih_vod_mekonialnie = models.BooleanField('Мекониальные', default=False)
    nepravilnoe_polojenie_ploda = models.ForeignKey(NepravilnoePolojeniePloda,
                                                    verbose_name='Неправильное положение плода',
                                                    on_delete=models.CASCADE, null=True,
                                                    blank=True)
    obvitie_pupovini = models.BooleanField('Есть', default=False)
    mnogoplodie = models.ForeignKey(Mnogoplodie, verbose_name='Многоплодие',
                                    on_delete=models.CASCADE, null=True,
                                    blank=True)
    krupniy_plod = models.BooleanField('Тазовое предлежание', default=False)
    predlejanie_placenti = models.ForeignKey(PredlejaniePlacenti, verbose_name='Предлежание плаценты',
                                             on_delete=models.CASCADE, null=True,
                                             blank=True)
    uroven_papp_a = models.ForeignKey(UrovenPappa, verbose_name='Уровень РАРР-А',
                                      on_delete=models.CASCADE, null=True,
                                      blank=True)
    uroven_beta_hgch = models.ForeignKey(UrovenBetaHgch, verbose_name='Уровень бета ХГЧ',
                                         on_delete=models.CASCADE, null=True,
                                         blank=True)
    fakt_provedeniya_uzi_10_14 = models.BooleanField('В срок 10-14 нед.', default=False)
    fakt_provedeniya_uzi_20_24 = models.BooleanField('В срок 20-24 нед.', default=False)
    fakt_provedeniya_uzi_32_34 = models.BooleanField('В срок 32-34 нед.', default=False)
    nesootvetstvie_dannih_uzi_soot = models.BooleanField(
        'Сост. ок. -плод.вод. (количество(ИАЖ), прозрачность, наличие взвеси, примес.', default=False)
    nesootvetstvie_dannih_uzi_fetomerii = models.BooleanField('Фетомерии (размеры плодного яйца, эмбриона, плода)',
                                                              default=False)
    nesootvetstvie_dannih_uzi_placenti = models.BooleanField('Плаценты/хориона (толщина, структура, степень зрелости)',
                                                             default=False)
    nalichie_vpr_po_rezultatam_uzi = models.ForeignKey(NalichieVprPoRezultatamUzi,
                                                       verbose_name='Наличие ВПР по результатам УЗИ',
                                                       on_delete=models.CASCADE, null=True,
                                                       blank=True)
    data_provedeniya_prenatalnogo_konsiliuma = models.DateField('Дата проведения пренатального консилиума', null=True,
                                                                blank=True)
    nomer_protokola = models.CharField('Номер протокола', max_length=255, null=True, blank=True)
    obshee_sostoyanie_ploda = models.ForeignKey(ObsheeSostoyaniePloda,
                                                verbose_name='Общее состояние плода',
                                                on_delete=models.CASCADE, null=True,
                                                blank=True)
    napravlena_na_extrennoe_rodorazreshenie = models.BooleanField('Да', default=False)
    diagnoz_osnovnoy_mkb10 = models.ForeignKey(MKB10,
                                               verbose_name='Диагноз основной (код по МКБ-10)',
                                               on_delete=models.CASCADE, null=True,
                                               blank=True)
    dopolnitelnie_zamechaniya_vracha = models.TextField('Текст рекомендации', null=True, blank=True)

    def __str__(self):
        return str(self.nomer_anketi)


class MestoIshoda(models.Model):
    class Meta:
        verbose_name = 'Место исхода'
        verbose_name_plural = 'Место исхода'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class StepenRiskaPosleIshoda(models.Model):
    class Meta:
        verbose_name = 'Степень риска после исхода'
        verbose_name_plural = 'Степень риска после исхода'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class GibelPloda(models.Model):
    class Meta:
        verbose_name = 'Гибель плода'
        verbose_name_plural = 'Гибель плода'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class IshodBeremennosti(models.Model):
    class Meta:
        verbose_name = 'Исход беременности'
        verbose_name_plural = 'Исход беременности'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class KesarevoSechenie1(models.Model):
    class Meta:
        verbose_name = 'Кесарево сечение (Исход1)'
        verbose_name_plural = 'Кесарево сечение (Исход1)'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class KesarevoSechenie2(models.Model):
    class Meta:
        verbose_name = 'Кесарево сечение (Исход2)'
        verbose_name_plural = 'Кесарево сечение (Исход2)'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class KesarevoSechenie3(models.Model):
    class Meta:
        verbose_name = 'Кесарево сечение (Исход3)'
        verbose_name_plural = 'Кесарево сечение (Исход3)'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Ishod(models.Model):
    class Meta:
        verbose_name = 'Исход'
        verbose_name_plural = 'Исход'

    data_ishoda = models.DateField('Дата исхода', null=True, blank=True)
    mesto_ishoda = models.ForeignKey(MestoIshoda, verbose_name='Место исхода',
                                     on_delete=models.CASCADE, null=True,
                                     blank=True)
    stepen_riska_posle_ishoda = models.ForeignKey(StepenRiskaPosleIshoda, verbose_name='Степень риска после исхода',
                                                  on_delete=models.CASCADE, null=True,
                                                  blank=True)
    gibel_ploda = models.ForeignKey(GibelPloda, verbose_name='Гибель плода',
                                    on_delete=models.CASCADE, null=True,
                                    blank=True)
    ishod_beremennosti = models.ForeignKey(IshodBeremennosti, verbose_name='Исход беременности',
                                           on_delete=models.CASCADE, null=True,
                                           blank=True)
    kesarevo_sechenie1 = models.ForeignKey(KesarevoSechenie1, verbose_name='Кесарево сечение',
                                           on_delete=models.CASCADE, null=True,
                                           blank=True)
    kesarevo_sechenie2 = models.ForeignKey(KesarevoSechenie2, verbose_name='Кесарево сечение',
                                           on_delete=models.CASCADE, null=True,
                                           blank=True)
    kesarevo_sechenie3 = models.ForeignKey(KesarevoSechenie3, verbose_name='Кесарево сечение',
                                           on_delete=models.CASCADE, null=True,
                                           blank=True)
    preeklampsiya = models.BooleanField('Преэклампсия', default=False)
    predlejanie_placenti = models.BooleanField('Предлежание плаценты', default=False)
    prejdevrem_otsloyka = models.BooleanField('Преждеврем. отслойка норм. расп. плаценты', default=False)
    anomalii_rodovoy_deyatelnosti = models.BooleanField('Аномалии родовой деятельности', default=False)
    klinicheski_uzkiy_taz = models.BooleanField('Клинически узкий таз', default=False)
    razriv_matki = models.BooleanField('Разрыв матки', default=False)
    dvc_sindrom = models.BooleanField('ДВС-синдром', default=False)
    emboliya = models.BooleanField('Эмболия', default=False)
    smert_materi = models.BooleanField('Смерть матери', default=False)
    data_smerti_materi = models.DateField('Дата смерти матери', null=True, blank=True)
    prichina_smerti_materi_mkb10 = models.ForeignKey(MKB10, verbose_name='Причина смерти матери по МКБ-10',
                                                     on_delete=models.CASCADE, null=True,
                                                     blank=True)

    def __str__(self):
        return str(self.data_ishoda)


class SmertNovorojdennogo(models.Model):
    class Meta:
        verbose_name = 'Смерть новорожденного'
        verbose_name_plural = 'Смерть новорожденного'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nazvanie


class Novorojdenniy(models.Model):
    class Meta:
        verbose_name = 'Новорожденный'
        verbose_name_plural = 'Новорожденныe'
    nomer_beremennoy = models.ForeignKey(Beremennaya, verbose_name='Беременная', on_delete=models.CASCADE, max_length=255, null=True, blank=True)
    nomer_novorojdennogo = models.CharField('Номер новорожденного', max_length=255, null=True, blank=True)
    pol_novorojdennogo = models.IntegerField('Пол новорожденного', choices=POL, null=True, blank=True)
    ves_novorojdennogo = models.CharField('Вес новорожденного', max_length=255, null=True, blank=True)
    rost_novorojdennogo = models.CharField('Рост новорожденного', max_length=255, null=True, blank=True)
    ocenka_po_shkale_apgar_na1_min = models.IntegerField('Оценка по шкале Апгар на 1 мин, баллы', null=True, blank=True)
    ocenka_po_shkale_apgar_na5_min = models.IntegerField('Оценка по шкале Апгар на 5 мин, баллы', null=True, blank=True)
    vpr_novorojdennogo_po_mkb10 = models.ForeignKey(MKB10, verbose_name='ВПР новорожденного (код по МКБ-10)',
                                                    on_delete=models.CASCADE, null=True,
                                                    blank=True)
    smert_novorojdennogo = models.ForeignKey(SmertNovorojdennogo, verbose_name='Смерть новорожденного',
                                             on_delete=models.CASCADE, null=True,
                                             blank=True)
    prichina_smerti_materi_po_mkb10 = models.ForeignKey(MKB10, related_name='smerti_novorojdennogo',
                                                        verbose_name='Причина смерти матери по МКБ-10',
                                                        on_delete=models.CASCADE, null=True,
                                                        blank=True)

    def __str__(self):
        return self.nomer_novorojdennogo


# Справочная модель Цель направления
class CelNapravleniya(models.Model):
    class Meta:
        verbose_name = 'Цель направления'
        verbose_name_plural = 'Цели направления'

    nazvanie = models.CharField(verbose_name='Название цели направления',
                                max_length=255, null=True,
                                blank=True)

    def __str__(self):
        return self.nazvanie


# Направление
class Napravlenie(models.Model):
    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    nomer_beremennoy = models.ForeignKey(Beremennaya, verbose_name='Номер беременной',
                                         on_delete=models.CASCADE, null=True,
                                         blank=True)
    cel_napravleniya = models.ForeignKey(CelNapravleniya, verbose_name='Цель направления',
                                         on_delete=models.CASCADE, null=True,
                                         blank=True)
    punkt_napravleniya = models.ForeignKey(MedOrganizacia, verbose_name='Пункт направления',
                                           on_delete=models.CASCADE, null=True,
                                           blank=True)
    predpolagaemyi_diagnoz = models.TextField('Текст предполагаемого диагноза',
                                              null=True, blank=True)
    diagnoz_podtverjden = models.BooleanField('Диагноз подтвержден? Да/Нет',
                                              default=False, null=True, blank=True)
    data = models.DateField('Дата явки беременной в ЖК с результатом направления',
                            null=True, blank=True)

    def __str__(self):
        return str(self.nomer_beremennoy)


# Консультация (номер беременной для привязке к анкете,
# отправлено и отправитель (из отправителя подгружается роль и его мед учреждение,
# для вывода в таблицу списка консультаций
class Konsultaciaya(models.Model):
    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

    nomer_beremennoy = models.ForeignKey(Beremennaya, verbose_name='Номер беременной',
                                         on_delete=models.CASCADE, null=True,
                                         blank=True)
    otpravleno = models.DateField('Отправлено (дата отправления)',
                                  null=True, blank=True)
    otpravitel = models.ForeignKey(Polzovateli, verbose_name='Отправитель (роль)',
                                   on_delete=models.CASCADE, null=True,
                                   blank=True)

    tema = models.CharField('Тема', max_length=255, null=True, blank=True)
    soobshenie = models.TextField('Сообщение', null=True, blank=True)
    egp = models.BooleanField('ЭГП', default=False, null=True, blank=True)
    oaa = models.BooleanField('ОАА', default=False, null=True, blank=True)
    rubec_na_matke = models.BooleanField('Рубец на матке',
                                         default=False, null=True, blank=True)
    rh_sensibilizaciya = models.BooleanField('Rh-сенсибилизация',
                                             default=False, null=True, blank=True)
    prochie = models.TextField('Прочие', null=True, blank=True)

    def __str__(self):
        return str(self.nomer_beremennoy)


# Смена ЖК у беременной (стр 63 Скрины.doc)
class Smena_JK_u_beremennoy(models.Model):
    class Meta:
        verbose_name_plural = 'Смена ЖК у беременной'

    nomer_beremennoy = models.ForeignKey(Beremennaya, verbose_name='Номер анкеты',
                                         on_delete=models.CASCADE, null=True,
                                         blank=True)
    novaya_JK = models.ForeignKey(MedOrganizacia, verbose_name='Новая ЖК',
                                  on_delete=models.CASCADE, null=True,
                                  blank=True)
    prichina = models.TextField('Причина', null=True, blank=True)

    def __str__(self):
        return str(self.nomer_beremennoy)
