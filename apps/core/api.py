from django.db.models import Q
from rest_framework import viewsets, generics

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Rayon, Beremennaya, Doctor, Novorojdenniy, Napravlenie, Konsultaciaya, MKB10
from apps.core.serializers import RayonSerializer, BeremennayaSerializer, DoctorSerializer, NovorojdenniySerializer, \
    NapravlenieSerializer, KonsultaciayaSerializer, MKB10Serializer


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
