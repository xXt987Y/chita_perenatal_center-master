from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Rayon, Beremennaya, Doctor, Novorojdenniy, Napravlenie, Konsultaciaya, MKB10, \
    Smena_JK_u_beremennoy, Anketa, ROL, Otchety
from apps.core.serializers import RayonSerializer, BeremennayaSerializer, DoctorSerializer, NovorojdenniySerializer, \
    NapravlenieSerializer, KonsultaciayaSerializer, MKB10Serializer, SmenaJKSerializer, AnketaSerializer, \
    OtchetySerializer


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
        beremennaya = Beremennaya.objects.get(id=pk)
        novorojdenniy = beremennaya.novorojdenniy_set.all()
        serializer = NovorojdenniySerializer(novorojdenniy, many=True)
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
        napravlenie = napravlenie.filter(napravlenie_pometka_na_udalenie=False)
        serializer = NapravlenieSerializer(napravlenie, many=True)
        return Response(serializer.data)


class NapravlenieViewSetDV(APIView):
    authentication_classes = []
    serializer_class = NapravlenieSerializer

    def post(self, request, pk):
        napravlenie = get_object_or_404(Napravlenie, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=napravlenie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        beremennaya = Beremennaya.objects.get(id=pk)
        napravlenie = beremennaya.napravlenie_set.all()
        serializer = NapravlenieSerializer(napravlenie, many=True)
        return Response(serializer.data)


class NapravlenieViewSetDV2(APIView):
    serializer_class = NapravlenieSerializer

    def post(self, request, pk):
        napravlenie = get_object_or_404(Napravlenie, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=napravlenie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        napravlenie = Napravlenie.objects.get(pk=pk)
        serializer = NapravlenieSerializer(napravlenie, many=False)
        return Response(serializer.data)







class KonsultaciayaViewSetDV2(APIView):
    serializer_class = KonsultaciayaSerializer

    def post(self, request, pk):
        konsultaciaya = get_object_or_404(Konsultaciaya, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=konsultaciaya)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        beremennaya=Beremennaya.objects.get(id=pk)
        konsultaciaya = beremennaya.konsultaciaya_set.all()
        serializer = KonsultaciayaSerializer(konsultaciaya, many=True)
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
        self.authentication_classes = []
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
        anketa = anketa.filter(anketa_pometka_na_udalenie=False)
        serializer = AnketaSerializer(anketa, many=True)
        return Response(serializer.data)


class AnketaViewSetDV(APIView):
    serializer_class = AnketaSerializer

    def post(self, request, pk):
        anketa = get_object_or_404(Anketa, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=anketa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        beremennaya=Beremennaya.objects.get(id=pk)
        anketa = beremennaya.anketa_set.all()
        serializer = AnketaSerializer(anketa, many=True)
        return Response(serializer.data)


class AnketaViewSetLV2(APIView):
    serializer_class = AnketaSerializer

    def post(self, request):
        self.authentication_classes = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NapravlenieViewSetLV2(APIView):
    serializer_class = NapravlenieSerializer

    def post(self, request):
        self.authentication_classes = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KonsultaciayaViewSetLV2(APIView):
    serializer_class = KonsultaciayaSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['otpravitel'] = request.user.polzovatel

            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmenaJKViewSetLV2(APIView):
    serializer_class = SmenaJKSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NovorojdenniyViewSetLV2(APIView):
    serializer_class = NovorojdenniySerializer

    def post(self, request):
        self.authentication_classes = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OtchetyViewSetLV(APIView):

    def get(self, request):
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Doctor._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        otchety = Otchety.objects.filter(or_condition)

        serializer = OtchetySerializer(otchety, many=True)
        return Response(serializer.data)


class OtchetyViewSetDV(APIView):

    def get(self, request, pk):
        otchety = Otchety.objects.get(pk=pk)
        serializer = OtchetySerializer(otchety, many=False)
        return Response(serializer.data)