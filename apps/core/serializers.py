from rest_framework import serializers

from apps.core.models import Rayon, Beremennaya, Doctor, Novorojdenniy, Napravlenie, Konsultaciaya, MKB10


class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = '__all__'

    stepen_riska = serializers.SerializerMethodField()
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

    def get_stepen_riska_title(self, obj):
        return obj.stepen_riska.nazvanie


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class NovorojdenniySerializer(serializers.ModelSerializer):
    class Meta:
        model = Novorojdenniy
        fields = '__all__'


class NapravlenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Napravlenie
        fields = '__all__'


class KonsultaciayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konsultaciaya
        fields = '__all__'
    # otpravitel_title = serializers.SerializerMethodField()
    #
    # def get_otpravitel_title(self, obj):
    #     return obj.otpravitel.med_organiizaciya

class MKB10Serializer(serializers.ModelSerializer):
    class Meta:
        model = MKB10
        fields = '__all__'