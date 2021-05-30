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

class BeremennayaFormPart2(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = [
            'vrednie_privichki_kurenie',
            'vrednie_privichki_alco',
            'vrednie_privichki_narko',
            'vrednie_privichki_toxi',
        ]