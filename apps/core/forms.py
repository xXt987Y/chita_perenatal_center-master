from django import forms

from apps.core.models import Beremennaya, Anketa, Ishod


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


class BeremennayaVredniePrivichki(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'vrednie_privichki_kurenie',
            'vrednie_privichki_alco',
            'vrednie_privichki_narko',
            'vrednie_privichki_toxi',
        ]

class BeremennayaVrednieFactori(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'vrednie_factori_truda_himicheskie',
            'vrednie_factori_truda_radioactiv',
            'vrednie_factori_truda_priem_lekarstvennih_sredstv',
            'vrednie_factori_truda_neudvl_jil_ysloviya',
        ]

class AnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = '__all__'

class IshodForm(forms.ModelForm):
    class Meta:
        model = Ishod
        fields = '__all__'

    data_ishoda = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))



class BeremennayaForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = '__all__'


class BeremennayaInfekcionnieBolezniForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'infekcionnie_bolezni_gripp',
            'infekcionnie_bolezni_sifilis',
            'infekcionnie_bolezni_vich',
            'infekcionnie_bolezni_krasnuha',
            'infekcionnie_bolezni_orvi',
            'infekcionnie_bolezni_tuberkulez',
            'infekcionnie_bolezni_virusniy_gepatit',
            'infekcionnie_bolezni_toksoplazmoz',
            'infekcionnie_bolezni_virusniy_cmvi',
        ]


class BeremennayaRazmerTazaForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'razmer_taza_ds',
            'razmer_taza_dc',
            'razmer_taza_dt',
            'razmer_taza_cd',
            'razmer_taza_ce',
            'razmer_taza_cv',
        ]


class BeremennayaZabolevanieVnutForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'zabolevanie_vnut_pol_organov_vospalenie_roj',
            'zabolevanie_vnut_pol_organov_opuhl',
            'zabolevanie_vnut_pol_organov_mioma',
            'zabolevanie_vnut_pol_organov_gipoplaziya',
            'zabolevanie_vnut_pol_organov_poroki',
            'zabolevanie_vnut_pol_organov_operacii_pred',
            'zabolevanie_vnut_pol_organov_operacii_matk',
            'zabolevanie_vnut_pol_organov_istmiko',
            'zabolevanie_vnut_pol_organov_onkologiya',
        ]


class BeremennayaOslojneniyaBeremennostiForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'oslojneniya_beremennosti_anemez',
            'oslojneniya_beremennosti_anemez_fetoplacent',
            'oslojneniya_beremennosti_anemez_obostrenie',
            'oslojneniya_beremennosti_anemez_prejdevremennoy',
            'oslojneniya_rodov',
        ]


class BeremennayaOslojneniyaRodovForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'oslojneniya_rodov',
            'oslojneniya_rodov_osl_razrivom',
            'oslojneniya_rodov_osl_krovotech',
            'oslojneniya_rodov_osl_gnoyno',
            'oslojneniya_rodov_osl_mertvoroj',
            'kesarevo_sechenie',
            'rubec_na_matke',
            'oslojneniya_anomaliyami_rodovoy_deyatelnosti',
            'klinicheski_uzkiy_taz',
            'plodorazrushayushaya_operaciya',
        ]


class BeremennayaNovorojdenniyPlodForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'novorojdenniy_plod_smert',
            'novorojdenniy_plod_ves',
            'novorojdenniy_plod_nevrolgiych',
            'novorojdenniy_plod_vpr',
            'novorojdenniy_plod_perinatalnie',
        ]


class BeremennayaBolezniEndokrForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'saharniy_diabed',
            'gestacionniy_saharniy_diabed',
            'zabolevanie_shitovidnoy',
            'ako',
            'deincifalniy_sindrom',
        ]


class BeremennayaBolezniKroviForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'bolezni_krovi_anemiya',
            'bolezni_krovi_trombocitopeniya',
            'bolezni_krovi_trombozi',
            'koagulopatiya',
        ]


class BeremennayaPsihRastroystvaForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'psih_rastroystva_psihozi',
            'psih_rastroystva_narusheniya_lich',
            'psih_rastroystva_shizofreniya',
            'psih_rastroystva_umstvennaya_otstalost',
        ]


class BeremennayaBolezniNsForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'bolezni_nervnoy_sistemi_nasledstvennie',
            'bolezni_nervnoy_sistemi_vospalitelnie',
            'bolezni_nervnoy_sistemi_miopiya',
            'bolezni_nervnoy_narushenie',
            'bolezni_nervnoy_chmt',
        ]


class BeremennayaBolezniSistemiKrovoobForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'bolezni_sistemi_krovoob_poroki_serdca_bez',
            'bolezni_sistemi_krovoob_poroki_serdca_c',
            'bolezni_sistemi_krovoob_miokarda',
            'bolezni_sistemi_krovoob_sosudov',
            'bolezni_sistemi_krovoob_narush',
            'bolezni_sistemi_krovoob_operirovannoe',
            'bolezni_sistemi_krovoob_gipertoniya',
        ]


class BeremennayaBolezniOrganovDihaniyaForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'bolezni_organov_dihaniya_astma',
            'bolezni_organov_dihaniya_pnevmoniya',
            'bolezni_organov_dihaniya_bronh',
            'bolezni_organov_dihaniya_lobektomiya',
        ]


class BeremennayaBolezniOrganovMochForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'bolezni_organov_mochv_glomer',
            'bolezni_organov_mochv_pochka',
            'bolezni_organov_mochv_tuberkulez',
            'bolezni_organov_mochv_hpn',
            'bolezni_organov_mochv_gidronefroz',
            'bolezni_organov_mochv_polikistoz',
        ]
