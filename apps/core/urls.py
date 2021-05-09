from django.urls import path, include
from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'rayon', RayonViewSet)
from apps.core.api import RayonViewSetLV, RayonViewSetDV, BeremennayaViewSetLV, BeremennayaViewSetDV, DoctorViewSetLV, \
    DoctorViewSetDV, NovorojdenniyViewSetLV, NovorojdenniyViewSetDV, NapravlenieViewSetLV, NapravlenieViewSetDV, \
    KonsultaciayaViewSetLV, KonsultaciayaViewSetDV, MKB10ViewSetLV, MKB10ViewSetDV

from apps.core.views import home, sbor_znachenii_spravocnix_tabliz

urlpatterns = [
    path('api/rayon/', RayonViewSetLV.as_view()),
    path('api/rayon/<int:pk>', RayonViewSetDV.as_view()),
    path('api/beremennaya/', BeremennayaViewSetLV.as_view()),
    path('api/beremennaya/<int:pk>', BeremennayaViewSetDV.as_view()),
    path('api/doctor/', DoctorViewSetLV.as_view()),
    path('api/doctor/<int:pk>', DoctorViewSetDV.as_view()),
    path('api/novorojdenniy/', NovorojdenniyViewSetLV.as_view()),
    path('api/novorojdenniy/<int:pk>', NovorojdenniyViewSetDV.as_view()),
    path('api/napravlenie/', NapravlenieViewSetLV.as_view()),
    path('api/napravlenie/<int:pk>', NapravlenieViewSetDV.as_view()),
    path('api/konsultaciaya/', KonsultaciayaViewSetLV.as_view()),
    path('api/konsultaciaya/<int:pk>', KonsultaciayaViewSetDV.as_view()),
    path('api/mkb10/', MKB10ViewSetLV.as_view()),
    path('api/mkb10/<int:pk>', MKB10ViewSetDV.as_view()),
    path('api/sbor_znachenii_spravocnix_tabliz', sbor_znachenii_spravocnix_tabliz),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),
]
