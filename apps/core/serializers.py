from rest_framework import serializers

from apps.core.models import Rayon, Beremennaya, Doctor, Novorojdenniy, Napravlenie, Konsultaciaya, MKB10, \
    Smena_JK_u_beremennoy, UrovenMedObsluzivaniya, TipOrganizacii, MedOrganizacia, StepenRiska, SemeynoePolojenie, \
    GeneticheskieFaktori, MenstrualnayaFunkciya, Besplodie, TipBesplodiya, NastuplenieBeremennostiVRezultate, \
    ParitetBeremennosti, SamoproizvolniyAbort, IskustvenniyAbort, OslojneniyaIskustvenniyAbort, KesarevoSechenie, \
    SaharniyDiabed, GestacionniySaharniyDiabed, ZabolevanieShitovidnoy, AKO, Koagulopatiya, FormaSujeniyaTaza, \
    StepenSujeniyaTaza, VzyataPodNabludenie, OslojneniyaRodov, Mnogoplodie, NepravilnoePolojeniePloda, \
    FetoplacentarnayaNedostatochnost, RezusSensibilizaciya, Preeklampsiya, PredlejaniePlacenti, UrovenPappa, \
    UrovenBetaHgch, NalichieVprPoRezultatamUzi, ObsheeSostoyaniePloda, MestoIshoda, GibelPloda, IshodBeremennosti, \
    CelNapravleniya, SmertNovorojdennogo, KesarevoSechenie3, KesarevoSechenie2, KesarevoSechenie1, Anketa, \
    StepenRiskaPosleIshoda


class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = '__all__'


class UrovenMedObsluzivaniyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrovenMedObsluzivaniya
        fields = '__all__'


class TipOrganizaciiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipOrganizacii
        fields = '__all__'


class MedOrganizaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedOrganizacia
        fields = '__all__'


class StepenRiskaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepenRiska
        fields = '__all__'


class SemeynoePolojenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemeynoePolojenie
        fields = '__all__'


class GeneticheskieFaktoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneticheskieFaktori
        fields = '__all__'


class MenstrualnayaFunkciyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenstrualnayaFunkciya
        fields = '__all__'


class BesplodieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Besplodie
        fields = '__all__'


class TipBesplodiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipBesplodiya
        fields = '__all__'


class NastuplenieBeremennostiVRezultateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NastuplenieBeremennostiVRezultate
        fields = '__all__'


class ParitetBeremennostiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParitetBeremennosti
        fields = '__all__'


class SamoproizvolniyAbortSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamoproizvolniyAbort
        fields = '__all__'


class IskustvenniyAbortSerializer(serializers.ModelSerializer):
    class Meta:
        model = IskustvenniyAbort
        fields = '__all__'


class OslojneniyaIskustvenniyAbortSerializer(serializers.ModelSerializer):
    class Meta:
        model = OslojneniyaIskustvenniyAbort
        fields = '__all__'


class KesarevoSechenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = KesarevoSechenie
        fields = '__all__'


class SaharniyDiabedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaharniyDiabed
        fields = '__all__'


class GestacionniySaharniyDiabedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestacionniySaharniyDiabed
        fields = '__all__'


class ZabolevanieShitovidnoySerializer(serializers.ModelSerializer):
    class Meta:
        model = ZabolevanieShitovidnoy
        fields = '__all__'


class AKOSerializer(serializers.ModelSerializer):
    class Meta:
        model = AKO
        fields = '__all__'


class KoagulopatiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Koagulopatiya
        fields = '__all__'


class FormaSujeniyaTazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaSujeniyaTaza
        fields = '__all__'


class StepenSujeniyaTazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepenSujeniyaTaza
        fields = '__all__'


class VzyataPodNabludenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = VzyataPodNabludenie
        fields = '__all__'


class OslojneniyaRodovSerializer(serializers.ModelSerializer):
    class Meta:
        model = OslojneniyaRodov
        fields = '__all__'


class PreeklampsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preeklampsiya
        fields = '__all__'


class RezusSensibilizaciyaRodovSerializer(serializers.ModelSerializer):
    class Meta:
        model = RezusSensibilizaciya
        fields = '__all__'


class FetoplacentarnayaNedostatochnostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FetoplacentarnayaNedostatochnost
        fields = '__all__'


class NepravilnoePolojeniePlodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NepravilnoePolojeniePloda
        fields = '__all__'


class MnogoplodieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mnogoplodie
        fields = '__all__'


class PredlejaniePlacentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredlejaniePlacenti
        fields = '__all__'


class UrovenPappaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrovenPappa
        fields = '__all__'


class UrovenBetaHgchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrovenBetaHgch
        fields = '__all__'


class NalichieVprPoRezultatamUziSerializer(serializers.ModelSerializer):
    class Meta:
        model = NalichieVprPoRezultatamUzi
        fields = '__all__'


class ObsheeSostoyaniePlodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObsheeSostoyaniePloda
        fields = '__all__'


class MestoIshodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MestoIshoda
        fields = '__all__'


class GibelPlodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GibelPloda
        fields = '__all__'


class StepenRiskaPosleIshodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepenRiskaPosleIshoda
        fields = '__all__'


class IshodBeremennostiPappaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IshodBeremennosti
        fields = '__all__'


class KesarevoSechenie1Serializer(serializers.ModelSerializer):
    class Meta:
        model = KesarevoSechenie1
        fields = '__all__'


class KesarevoSechenie2Serializer(serializers.ModelSerializer):
    class Meta:
        model = KesarevoSechenie2
        fields = '__all__'


class KesarevoSechenie3Serializer(serializers.ModelSerializer):
    class Meta:
        model = KesarevoSechenie3
        fields = '__all__'


class SmertNovorojdennogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmertNovorojdennogo
        fields = '__all__'


class CelNapravleniyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelNapravleniya
        fields = '__all__'


class BeremennayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beremennaya
        fields = '__all__'

    stepen_riska_title = serializers.SerializerMethodField()
    jk_beremennoy_title = serializers.SerializerMethodField()
    data_vzyatiya_str = serializers.SerializerMethodField()


    def get_stepen_riska_title(self, obj):
        if obj.stepen_riska:
            return obj.stepen_riska.nazvanie


    def get_jk_beremennoy_title(self, obj):
        if obj.jk_beremennoy:
            return obj.jk_beremennoy.nazvanie

    def get_data_vzyatiya_str(self, obj):
        if obj.data_vzyatiya:
            return obj.data_vzyatiya.strftime("%d.%m.%Y")


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    med_organiizaciya_title = serializers.SerializerMethodField()

    def get_med_organiizaciya_title(self, obj):
        return obj.med_organiizaciya.nazvanie


class NovorojdenniySerializer(serializers.ModelSerializer):
    class Meta:
        model = Novorojdenniy
        fields = '__all__'

    pol_novorojdennogo_title = serializers.SerializerMethodField()

    def get_pol_novorojdennogo_title(self, obj):
        return obj.get_pol_novorojdennogo_display()


class NapravlenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Napravlenie
        fields = '__all__'

    punkt_napravleniya_title = serializers.SerializerMethodField()
    cel_napravleniya_title = serializers.SerializerMethodField()
    data_str = serializers.SerializerMethodField()

    def get_data_str(self, obj):
        return obj.data.strftime("%d.%m.%Y")

    def get_punkt_napravleniya_title(self, obj):
        return obj.punkt_napravleniya.nazvanie

    def get_cel_napravleniya_title(self, obj):
        return obj.cel_napravleniya.nazvanie


class KonsultaciayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konsultaciaya
        fields = '__all__'

    rol_otpavitelia_title = serializers.SerializerMethodField()
    med_organiizaciya_title = serializers.SerializerMethodField()
    otpravleno_str = serializers.SerializerMethodField()

    def get_otpravleno_str(self, obj):
        return obj.otpravleno.strftime("%d.%m.%Y")

    def get_rol_otpavitelia_title(self, obj):
        return obj.otpravitel.rol

    def get_med_organiizaciya_title(self, obj):
        return obj.otpravitel.med_organiizaciya.nazvanie


class MKB10Serializer(serializers.ModelSerializer):
    class Meta:
        model = MKB10
        fields = '__all__'


class SmenaJKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smena_JK_u_beremennoy
        fields = '__all__'

    nomer_beremennoy_title = serializers.SerializerMethodField()
    med_organiizaciya_title = serializers.SerializerMethodField()

    def get_nomer_beremennoy_title(self, obj):
        if __name__ == '__main__':
            return obj.nomer_beremennoy.nomer

    def get_med_organiizaciya_title(self, obj):
        return obj.novaya_JK.nazvanie


class AnketaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anketa
        fields = '__all__'

    familiya_vracha_title = serializers.SerializerMethodField()
    nomer_anketi_title = serializers.SerializerMethodField()
    data_zapolneniya_anketi_vrachem_str = serializers.SerializerMethodField()

    def get_familiya_vracha_title(self, obj):
        return obj.familiya_vracha.fio

    def get_nomer_anketi_title(self, obj):
        return obj.nomer_anketi.nomer

    def get_data_zapolneniya_anketi_vrachem_str(self, obj):
        return obj.data_zapolneniya_anketi_vrachem.strftime("%d.%m.%Y")