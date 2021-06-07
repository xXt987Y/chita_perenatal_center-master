from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from apps.core.forms import BeremennayaFormPart1, BeremennayaVredniePrivichki, BeremennayaForm, \
    BeremennayaVrednieFactori, BeremennayaInfekcionnieBolezniForm, BeremennayaRazmerTazaForm, \
    BeremennayaZabolevanieVnutForm, BeremennayaOslojneniyaBeremennostiForm, BeremennayaSomaticheskiePokazateliForm, \
    BeremennayaBolezniOrganovMochForm, BeremennayaBolezniOrganovDihaniyaForm, BeremennayaBolezniSistemiKrovoobForm, \
    BeremennayaBolezniNsForm, BeremennayaPsihRastroystvaForm, BeremennayaBolezniKroviForm, BeremennayaBolezniEndokrForm, \
    BeremennayaNovorojdenniyPlodForm, BeremennayaOslojneniyaRodovForm
from apps.core.models import Rayon, Beremennaya, Doctor, Novorojdenniy, Napravlenie, Konsultaciaya, MKB10, \
    Smena_JK_u_beremennoy, Anketa
from apps.core.serializers import RayonSerializer, BeremennayaSerializer, DoctorSerializer, NovorojdenniySerializer, \
    NapravlenieSerializer, KonsultaciayaSerializer, MKB10Serializer, SmenaJKSerializer, AnketaSerializer


# class RayonViewSet(viewsets.ModelViewSet):
#     queryset = Rayon.objects.all()
#     serializer_class = RayonSerializer
#     filter_backends = [DjangoFilterBackend]
#

class RayonViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Rayon._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                # это код для фильтрации уникальных полей
                # if key == 'data_lte':
                #     tmp_key = '{key}__lte'
                # if key == 'data_gte':
                #     tmp_key = '{key}__gte'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        rayon = Rayon.objects.filter(or_condition)

        serializer = RayonSerializer(rayon, many=True)
        return Response(serializer.data)


class RayonViewSetDV(APIView):

    def get(self, request, pk):
        rayon = Rayon.objects.get(pk=pk)
        serializer = RayonSerializer(rayon, many=False)
        return Response(serializer.data)



class BeremennayaViewSetLV(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        raise Exception('ПОСТ пошёл')
        return Response(status='200')

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Beremennaya._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                # это код для фильтрации уникальных полей
                # if key == 'data_lte':
                #     tmp_key = '{key}__lte'
                # if key == 'data_gte':
                #     tmp_key = '{key}__gte'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        rayon = Beremennaya.objects.filter(or_condition)

        serializer = BeremennayaSerializer(rayon, many=True)
        return Response(serializer.data)


class BeremennayaViewSetDV(APIView):
    authentication_classes = []
    def post(self, request, pk):
        beremenia = Beremennaya.objects.get(pk=pk)

        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        #
        # data = body
        # beremenia.fio = data['fio']
        # beremenia.nomer = data['nomer']
        # beremenia.save()
        # beremenia.fio = data['stepen_riska']
        # beremenia.fio = data['jk_beremennoy']
        # beremenia.fio = data['data_vzyatiya']
        # form = BeremennayaFormPart1(request.POST, instance=beremenia).save()
        # beremennaya_vrednie_privichki_form = BeremennayaVredniePrivichki(request.POST, instance=beremenia).save()
        # beremennaya_vrednie_factori_form = BeremennayaVrednieFactori(request.POST, instance=beremenia).save()
        # beremennaya_form = BeremennayaForm(request.POST, instance=beremenia).save()
        #
        # beremennaya_infekcionnie_bolezni_form = BeremennayaInfekcionnieBolezniForm(request.POST, instance=beremenia).save()
        # beremennaya_razmer_taza_form = BeremennayaRazmerTazaForm(request.POST, instance=beremenia).save()
        # beremennaya_zabolevanie_vnut_form = BeremennayaZabolevanieVnutForm(request.POST, instance=beremenia).save()
        # beremennayao_oslojneniya_beremennosti_form = BeremennayaOslojneniyaBeremennostiForm(request.POST, instance=beremenia).save()
        #
        # beremennayao_oslojneniya_rodov_form = BeremennayaOslojneniyaRodovForm(request.POST, instance=beremenia).save()
        # beremennayao_novorojdenniy_plod_form = BeremennayaNovorojdenniyPlodForm(request.POST, instance=beremenia).save()
        # beremennaya_bolezni_endokr_form = BeremennayaBolezniEndokrForm(request.POST, instance=beremenia).save()
        # beremennaya_bolezni_krovi_form = BeremennayaBolezniKroviForm(request.POST, instance=beremenia).save()
        #
        # beremennaya_bolezni_krovi_form = BeremennayaBolezniKroviForm(request.POST, instance=beremenia).save()
        # beremennaya_psih_rastroystva_form = BeremennayaPsihRastroystvaForm(request.POST, instance=beremenia).save()
        # beremennaya_bolezni_ns_form = BeremennayaBolezniNsForm(request.POST, instance=beremenia).save()
        # beremennaya_bolezni_sistemi_krovoob_form = BeremennayaBolezniSistemiKrovoobForm(request.POST, instance=beremenia).save()
        #
        # beremennaya_bolezni_organov_dihaniya_form = BeremennayaBolezniOrganovDihaniyaForm(request.POST, instance=beremenia).save()
        # beremennaya_bolezni_organov_moch_form = BeremennayaBolezniOrganovMochForm(request.POST, instance=beremenia).save()
        # beremennaya_somaticheskie_pokazateli_form = BeremennayaSomaticheskiePokazateliForm(request.POST, instance=beremenia).save()
        return Response(status=200)
        # Beremennaya.up

    def get(self, request, pk):
        rayon = Beremennaya.objects.get(pk=pk)
        serializer = BeremennayaSerializer(rayon, many=False)
        return Response(serializer.data)


class DoctorViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Doctor._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        doctor = Doctor.objects.filter(or_condition)

        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)


class DoctorViewSetDV(APIView):

    def get(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data)


class NovorojdenniyViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Novorojdenniy._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'

                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        novorojdenniy = Novorojdenniy.objects.filter(or_condition)

        serializer = NovorojdenniySerializer(novorojdenniy, many=True)
        return Response(serializer.data)


class NovorojdenniyViewSetDV(APIView):

    def get(self, request, pk):
        novorojdenniy = Novorojdenniy.objects.get(pk=pk)
        serializer = NovorojdenniySerializer(novorojdenniy, many=False)
        return Response(serializer.data)


class NapravlenieViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Napravlenie._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'

                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        napravlenie = Napravlenie.objects.filter(or_condition)

        serializer = NapravlenieSerializer(napravlenie, many=True)
        return Response(serializer.data)


class NapravlenieViewSetDV(APIView):

    def get(self, request, pk):
        napravlenie = Napravlenie.objects.get(pk=pk)
        serializer = NapravlenieSerializer(napravlenie, many=False)
        return Response(serializer.data)


class KonsultaciayaViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Konsultaciaya._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'

                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        konsultaciaya = Konsultaciaya.objects.filter(or_condition)

        serializer = KonsultaciayaSerializer(konsultaciaya, many=True)
        return Response(serializer.data)


class KonsultaciayaViewSetDV(APIView):

    def get(self, request, pk):
        konsultaciaya = Konsultaciaya.objects.get(pk=pk)
        serializer = KonsultaciayaSerializer(konsultaciaya, many=False)
        return Response(serializer.data)


class MKB10ViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Doctor._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        mkb10 = MKB10.objects.filter(or_condition)

        serializer = MKB10Serializer(mkb10, many=True)
        return Response(serializer.data)


class MKB10ViewSetDV(APIView):

    def get(self, request, pk):
        mkb10 = MKB10.objects.get(pk=pk)
        serializer = MKB10Serializer(mkb10, many=False)
        return Response(serializer.data)

class SmenaJKViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Doctor._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        smenaJK = Smena_JK_u_beremennoy.objects.filter(or_condition)

        serializer = SmenaJKSerializer(smenaJK, many=True)
        return Response(serializer.data)

class SmenaJKViewSetDV(APIView):

    def get(self, request, pk):
        smenaJK = Smena_JK_u_beremennoy.objects.get(pk=pk)
        serializer = SmenaJKSerializer(smenaJK, many=False)
        return Response(serializer.data)


class AnketaViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Doctor._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        anketa = Anketa.objects.filter(or_condition)

        serializer = AnketaSerializer(anketa, many=True)
        return Response(serializer.data)

class AnketaViewSetDV(APIView):

    def get(self, request, pk):
        anketa = Anketa.objects.get(pk=pk)
        serializer = AnketaSerializer(anketa, many=False)
        return Response(serializer.data)
