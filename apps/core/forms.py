from django import forms

from apps.core.models import Beremennaya, Anketa, Ishod, Konsultaciaya, Napravlenie, Smena_JK_u_beremennoy


class BeremennayaFormPart1(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'nomer',
            'stepen_riska',
            'jk_beremennoy',
            'data_vzyatiya',
            'vrach',
            'fio',
            'data_rojdeniya',
            'vozrast',
            'mesto_postoyannogo_projivaniya',
            'nomer_telefona',
            'nomer_oms',
        ]

    data_vzyatiya = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата взятия')
    data_rojdeniya = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}),
                                     label='Дата рождения')


class BeremennayaVredniePrivichki(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'p110_vrednie_privichki_kurenie',
            'p120_vrednie_privichki_alco',
            'p130_vrednie_privichki_narko',
            'p140_vrednie_privichki_toxi',
        ]


class BeremennayaVrednieFactori(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'p150_vrednie_factori_truda_himicheskie',
            'p160_vrednie_factori_truda_radioactiv',
            'p180_vrednie_factori_truda_priem_lekarstvennih_sredstv',
            'p170_vrednie_factori_truda_neudvl_jil_ysloviya',
        ]


class AnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = '__all__'


    data_zapolneniya_anketi_vrachem = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата заполнения анкеты врачем')
    data_provedeniya_prenatalnogo_konsiliuma = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата проведения пренатального консилиума')

class KonsultaciayaForm(forms.ModelForm):
    class Meta:
        model = Konsultaciaya
        fields = '__all__'

    otpravleno = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата отправления')

class NapravlenieForm(forms.ModelForm):
    class Meta:
        model = Napravlenie
        fields = ['nomer_beremennoy',
                  'cel_napravleniya',
                  'punkt_napravleniya',
                  'predpolagaemyi_diagnoz',
                  'diagnoz_podtverjden',
                  'data',
                  ]

    data = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата явки беременной в ЖК с результатом направления')

class IshodForm(forms.ModelForm):
    class Meta:
        model = Ishod
        fields = '__all__'

    data_ishoda = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата исхода')


class BeremennayaForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = '__all__'

    data_pervogo_dnya_posledney_menstruacii = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}),
                                     label='Дата первого дня последней менструации')

class SmenaJKForm(forms.ModelForm):
    class Meta:
        model = Smena_JK_u_beremennoy
        fields = '__all__'


class BeremennayaInfekcionnieBolezniForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1070_infekcionnie_bolezni_gripp',
            'qf1090_infekcionnie_bolezni_sifilis',
            'qf1110_infekcionnie_bolezni_vich',
            'qf1130_infekcionnie_bolezni_krasnuha',
            'qf1080_infekcionnie_bolezni_orvi',
            'qf1100_infekcionnie_bolezni_tuberkulez',
            'qf1120_infekcionnie_bolezni_virusniy_gepatit',
            'qf1135_infekcionnie_bolezni_toksoplazmoz',
            'qf1136_infekcionnie_bolezni_virusniy_cmvi',
        ]


class BeremennayaRazmerTazaForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'p250_razmer_taza_ds',
            'p260_razmer_taza_dc',
            'p270_razmer_taza_dt',
            'p280_razmer_taza_cd',
            'p290_razmer_taza_ce',
            'p300_razmer_taza_cv',
        ]


class BeremennayaZabolevanieVnutForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'p380_zabolevanie_vnut_pol_organov_vospalenie_roj',
            'p390_zabolevanie_vnut_pol_organov_opuhl',
            'p400_zabolevanie_vnut_pol_organov_mioma',
            'p410_zabolevanie_vnut_pol_organov_gipoplaziya',
            'p420_zabolevanie_vnut_pol_organov_poroki',
            'p430_zabolevanie_vnut_pol_organov_operacii_pred',
            'p440_zabolevanie_vnut_pol_organov_operacii_matk',
            'p450_zabolevanie_vnut_pol_organov_istmiko',
            'p455_zabolevanie_vnut_pol_organov_onkologiya',
        ]


class BeremennayaOslojneniyaBeremennostiForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'op660_oslojneniya_beremennosti_anemez',
            'op670_oslojneniya_beremennosti_anemez_fetoplacent',
            'op680_oslojneniya_beremennosti_anemez_obostrenie',
            'op690_oslojneniya_beremennosti_anemez_prejdevremennoy',
            'op700_oslojneniya_rodov',
        ]


class BeremennayaOslojneniyaRodovForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'op700_oslojneniya_rodov',
            'op710_oslojneniya_rodov_osl_razrivom',
            'op720_oslojneniya_rodov_osl_krovotech',
            'op730_oslojneniya_rodov_osl_gnoyno',
            'op740_oslojneniya_rodov_osl_mertvoroj',
            'op750_kesarevo_sechenie',
            'op751_rubec_na_matke',
            'op760_oslojneniya_anomaliyami_rodovoy_deyatelnosti',
            'op770_klinicheski_uzkiy_taz',
            'op780_plodorazrushayushaya_operaciya',
        ]


class BeremennayaNovorojdenniyPlodForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'op790_novorojdenniy_plod_smert',
            'op800_novorojdenniy_plod_ves',
            'op810_novorojdenniy_plod_nevrolgiych',
            'op820_novorojdenniy_plod_vpr',
            'op830_novorojdenniy_plod_perinatalnie',
        ]



class BeremennayaBolezniEndokrForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1150_saharniy_diabed',
            'qf1151_gestacionniy_saharniy_diabed',
            'qf1170_zabolevanie_shitovidnoy',
            'qf1175_ako',
            'qf1160_deincifalniy_sindrom',
        ]


class BeremennayaBolezniKroviForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1180_bolezni_krovi_anemiya',
            'qf1200_bolezni_krovi_trombocitopeniya',
            'qf1210_bolezni_krovi_trombozi',
            'qf1190_koagulopatiya',
        ]


class BeremennayaPsihRastroystvaForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1220_psih_rastroystva_psihozi',
            'qf1240_psih_rastroystva_narusheniya_lich',
            'qf1230_psih_rastroystva_shizofreniya',
            'qf1250_psih_rastroystva_umstvennaya_otstalost',
        ]


class BeremennayaBolezniNsForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1260_bolezni_nervnoy_sistemi_nasledstvennie',
            'qf1270_bolezni_nervnoy_sistemi_vospalitelnie',
            'qf1280_bolezni_nervnoy_sistemi_miopiya',
            'qf1290_bolezni_nervnoy_narushenie',
            'qf1290_bolezni_nervnoy_narushenie',
        ]


class BeremennayaBolezniSistemiKrovoobForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1300_bolezni_sistemi_krovoob_poroki_serdca_bez',
            'qf1310_bolezni_sistemi_krovoob_poroki_serdca_c',
            'qf1320_bolezni_sistemi_krovoob_miokarda',
            'qf1330_bolezni_sistemi_krovoob_sosudov',
            'qf1340_bolezni_sistemi_krovoob_narush',
            'qf1350_bolezni_sistemi_krovoob_operirovannoe',
            'qf1360_bolezni_sistemi_krovoob_gipertoniya',
        ]


class BeremennayaBolezniOrganovDihaniyaForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1370_bolezni_organov_dihaniya_astma',
            'qf1380_bolezni_organov_dihaniya_pnevmoniya',
            'qf1390_bolezni_organov_dihaniya_bronh',
            'qf1400_bolezni_organov_dihaniya_lobektomiya',
        ]


class BeremennayaBolezniOrganovMochForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'qf1410_bolezni_organov_mochv_glomer',
            'qf1420_bolezni_organov_mochv_pochka',
            'qf1430_bolezni_organov_mochv_tuberkulez',
            'qf1440_bolezni_organov_mochv_hpn',
            'qf1450_bolezni_organov_mochv_gidronefroz',
            'qf1460_bolezni_organov_mochv_polikistoz',
        ]


class BeremennayaSomaticheskiePokazateliForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Beremennaya
        fields = [
            'p200_somaticheskie_pokazateli_muzskoy',
            'p210_somaticheskie_pokazateli_girsutizm',
        ]


class AnketaSrokBeremennostiForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Anketa
        fields = [
            'srok_beremennosti_po_obektivnim_dannim',
            'srok_beremennosti_po_dannim_uzi',
            'srok_beremennosti_po_pervomu',
        ]


class AnketaOsobennostiForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Anketa
        fields = [
            'osobennosti_protekaniya_beremennosti_krovynistie',
            'osobennosti_protekaniya_beremennosti_virazenniy_toxikoz',
            'osobennosti_protekaniya_beremennosti_krovotechenie',
        ]


class AnketaNarushenieForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Anketa
        fields = [
            'narushenie_okoplodnih_vod_mnogovodie',
            'narushenie_okoplodnih_vod_malovodie',
            'narushenie_okoplodnih_vod_mekonialnie',
        ]


class AnketaFaktForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Anketa
        fields = [
            'fakt_provedeniya_uzi_10_14',
            'fakt_provedeniya_uzi_20_24',
            'fakt_provedeniya_uzi_32_34',
        ]


class AnketaNesootvetstvieForm(forms.ModelForm):
    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s %(help_text)s%(label)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Anketa
        fields = [
            'nesootvetstvie_dannih_uzi_soot',
            'nesootvetstvie_dannih_uzi_fetomerii',
            'nesootvetstvie_dannih_uzi_placenti',
        ]
