from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from apps.core.models import Doctor, MKB10
from apps.core.serializers import DoctorSerializer


def home(request):
    return render(request, "partical/home.html")


def sbor_znachenii_spravocnix_tabliz():

    doctor = Doctor.objects.all()
    mkb10 = MKB10.objects.all()


    # return JsonResponse({
    #     'doctor':DoctorSerializer(doctor, many=True),
    #     # 'mkb10':mkb10
    # })