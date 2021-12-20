from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Beremennaya, ROL, Konsultaciaya, Anketa, Doctor, Napravlenie, Novorojdenniy
from apps.core.serializers import BeremennayaSerializer, KonsultaciayaSerializer, AnketaSerializer, \
    NapravlenieSerializer, NovorojdenniySerializer


# Список беременных
class BeremennayaViewSetLV(APIView):
    serializer_class = BeremennayaSerializer

    def get(self, request):
        or_condition = Q()
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
                beremennaya = beremennaya.filter(jk_beremennoy=request.user.polzovatel.med_organiizaciya)

        beremennaya = beremennaya.filter(beremennaya_pometka_na_udalenie=False)
        serializer = BeremennayaSerializer(beremennaya, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.authentication_classes = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Одна беременная
class BeremennayaViewSetDV(APIView):
    serializer_class = BeremennayaSerializer

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


# Список консультаций для одной беременной
class KonsultaciayaViewSetLV(APIView):
    serializer_class = KonsultaciayaSerializer

    def get(self, request, beremenya_id):
        get_object_or_404(Beremennaya, id=beremenya_id)
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Konsultaciaya._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'

                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        konsultaciaya = Konsultaciaya.objects.filter(or_condition)
        konsultaciaya = konsultaciaya.filter(nomer_beremennoy_id=beremenya_id)
        konsultaciaya = konsultaciaya.filter(konsultaciya_pometka_na_udalenie=False)
        serializer = KonsultaciayaSerializer(konsultaciaya, many=True)
        return Response(serializer.data)

    def post(self, request, beremenya_id,):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['otpravitel'] = request.user.polzovatel

            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Одна консультация
class KonsultaciayaViewSetDV(APIView):
    serializer_class = KonsultaciayaSerializer

    def post(self, request, beremenya_id, pk):
        konsultaciaya = get_object_or_404(Konsultaciaya, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=konsultaciaya)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, beremenya_id, pk):
        konsultaciaya = Konsultaciaya.objects.get(pk=pk)
        serializer = KonsultaciayaSerializer(konsultaciaya, many=False)
        return Response(serializer.data)


# Список анкет для одной беременной
class AnketaViewSetLV(APIView):
    serializer_class = AnketaSerializer

    def post(self, request, beremenya_id):
        self.authentication_classes = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, beremenya_id):
        beremennaya = get_object_or_404(Beremennaya, id=beremenya_id)
        or_condition = Q()
        spisok_polei = list(map(lambda x: x.attname, Doctor._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'
                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        anketa = Anketa.objects.filter(or_condition)
        anketa = anketa.filter(anketa_pometka_na_udalenie=False)
        anketa = anketa.filter(nomer_anketi=beremennaya)
        serializer = AnketaSerializer(anketa, many=True)
        return Response(serializer.data)


# Редактирование одной анкеты
class AnketaViewSetDV(APIView):
    serializer_class = AnketaSerializer

    def post(self, request, beremenya_id, pk):
        anketa = get_object_or_404(Anketa, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=anketa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, beremenya_id, pk):
        anketa = Anketa.objects.get(pk=pk)
        serializer = AnketaSerializer(anketa, many=False)
        return Response(serializer.data)


# Список направлений для одной беременной
class NapravlenieViewSetLV(APIView):
    serializer_class = NapravlenieSerializer

    def get(self, request, beremenya_id):
        beremennaya = get_object_or_404(Beremennaya, id=beremenya_id)
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Napravlenie._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'

                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        napravlenie = Napravlenie.objects.filter(or_condition)
        napravlenie = napravlenie.filter(napravlenie_pometka_na_udalenie=False)
        napravlenie = napravlenie.filter(nomer_beremennoy=beremennaya)
        serializer = NapravlenieSerializer(napravlenie, many=True)
        return Response(serializer.data)

    def post(self, request, beremenya_id):
        self.authentication_classes = []
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Редактирование одного направления
class NapravlenieViewSetDV(APIView):
    serializer_class = NapravlenieSerializer

    def post(self, request, beremenya_id, pk):
        napravlenie = get_object_or_404(Napravlenie, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=napravlenie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, beremenya_id, pk):
        napravlenie = Napravlenie.objects.get(pk=pk)
        serializer = NapravlenieSerializer(napravlenie, many=False)
        return Response(serializer.data)



# Список новорожденных для одной беременной
class NovorojdenniyViewSetLV(APIView):
    serializer_class = NovorojdenniySerializer

    def get(self, request, beremenya_id):
        beremennaya = get_object_or_404(Beremennaya, id=beremenya_id)
        or_condition = Q()

        spisok_polei = list(map(lambda x: x.attname, Novorojdenniy._meta.fields))
        for key, value in dict(request.query_params).items():
            if key in spisok_polei:
                tmp_key = f'{key}__contains'

                or_condition.add(Q(**{tmp_key: value[0]}), Q.OR)

        novorojdenniy = Novorojdenniy.objects.filter(or_condition)
        novorojdenniy = novorojdenniy.filter(nomer_beremennoy=beremennaya)
        serializer = NovorojdenniySerializer(novorojdenniy, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Редактирование одного новорожденного
class NovorojdenniyViewSetDV(APIView):

    def get(self, request, pk):
        beremennaya = Beremennaya.objects.get(id=pk)
        novorojdenniy = beremennaya.novorojdenniy_set.all()
        serializer = NovorojdenniySerializer(novorojdenniy, many=True)
        return Response(serializer.data)
