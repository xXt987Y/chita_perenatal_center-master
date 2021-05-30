from django import forms

from apps.core.models import Beremennaya


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