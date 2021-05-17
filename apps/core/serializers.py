from rest_framework import serializers

from apps.core.models import Rayon, Beremennaya, Doctor, Novorojdenniy, Napravlenie, Konsultaciaya, MKB10, \
    Smena_JK_u_beremennoy


class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = '__all__'

    # stepen_riska = serializers.SerializerMethodField()
    # uroven_type_name = serializers.SerializerMethodField()
    #

    #
    # def get_uroven_type_name(self, obj):
    #     return obj.get_uroven_type_display()


class BeremennayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beremennaya
        fields = '__all__'

    stepen_riska_title = serializers.SerializerMethodField()
    jk_beremennoy_title = serializers.SerializerMethodField()
    data_vzyatiya = serializers.SerializerMethodField()

    def get_stepen_riska_title(self, obj):
        return obj.stepen_riska.nazvanie

    def get_jk_beremennoy_title(self, obj):
        return obj.jk_beremennoy.nazvanie

    def get_data_vzyatiya(self, obj):
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

    def get_punkt_napravleniya_title(self, obj):
        return obj.punkt_napravleniya.nazvanie


class KonsultaciayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konsultaciaya
        fields = '__all__'

    rol_otpavitelia_title = serializers.SerializerMethodField()
    med_organiizaciya_title = serializers.SerializerMethodField()

    def get_rol_otpavitelia_title(self, obj):
        return obj.otpravitel.rol.nazvanie

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