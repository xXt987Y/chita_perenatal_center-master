from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status

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
    Smena_JK_u_beremennoy, Anketa, ROL
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


class BeremennayaViewSetLV2(APIView):
    authentication_classes = []
    serializer_class = BeremennayaSerializer
    def post(self, request):
        self.authentication_classes = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BeremennayaViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()
        beremennaya = []
        try:
            rol = request.user.polzovatel.rol
        except Exception:
            rol = None
        if rol:
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

            beremennaya = Beremennaya.objects.filter(or_condition)

            if rol == ROL.VRACH_ZK or rol == ROL.ADMIN_ZK or rol == ROL.KONSULTANT_ZK:
                beremennaya = beremennaya.filter(jk_beremennoy= request.user.polzovatel.med_organiizaciya)


        serializer = BeremennayaSerializer(beremennaya, many=True)
        return Response(serializer.data)


class BeremennayaViewSetDV(APIView):
    authentication_classes = []
    serializer_class = BeremennayaSerializer

    @csrf_exempt
    def post(self, request, pk):
        beremenia = get_object_or_404(Beremennaya, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=beremenia)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
    authentication_classes = []
    serializer_class = AnketaSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    authentication_classes = []
    serializer_class = AnketaSerializer

    @csrf_exempt
    def post(self, request, pk):
        anketa = get_object_or_404(Anketa, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=anketa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        anketa = Anketa.objects.get(pk=pk)
        serializer = AnketaSerializer(anketa, many=False)
        return Response(serializer.data)
