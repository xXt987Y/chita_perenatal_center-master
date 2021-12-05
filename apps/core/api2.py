
# Список беременных
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import Beremennaya, ROL, Konsultaciaya
from apps.core.serializers import BeremennayaSerializer, KonsultaciayaSerializer


class BeremennayaViewSetLV(APIView):

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
