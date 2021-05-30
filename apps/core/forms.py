from django import forms

from apps.core.models import Beremennaya


class BeremennayaForm(forms.ModelForm):
    class Meta:
        model = Beremennaya
        fields = '__all__'
