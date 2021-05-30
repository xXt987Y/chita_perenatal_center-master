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

class BeremennayaVrednieFactori(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'vrednie_factori_truda_himicheskie',
            'vrednie_factori_truda_radioactiv',
            'vrednie_factori_truda_priem_lekarstvennih_sredstv',
            'vrednie_factori_truda_neudvl_jil_ysloviya',
        ]