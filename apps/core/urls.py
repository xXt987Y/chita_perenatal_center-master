from django.urls import path

# router = routers.DefaultRouter()
# router.register(r'rayon', RayonViewSet)
from apps.core.api import RayonViewSetLV, RayonViewSetDV, DoctorViewSetLV, \
    DoctorViewSetDV, MKB10ViewSetLV, MKB10ViewSetDV,  OtchetyViewSetLV, OtchetyViewSetDV
from apps.core.api2 import BeremennayaViewSetLV, BeremennayaViewSetDV, KonsultaciayaViewSetLV, KonsultaciayaViewSetDV, \
    AnketaViewSetLV, AnketaViewSetDV, NapravlenieViewSetLV, NapravlenieViewSetDV, NovorojdenniyViewSetLV, \
    NovorojdenniyViewSetDV, SmenaJKViewSetLV, SmenaJKViewSetDV
from apps.core.views import home, sbor_znachenii_spravocnix_tabliz, vhod, vihod, loginpage

urlpatterns = [
    path('api/sbor_znachenii_spravocnix_tabliz/', sbor_znachenii_spravocnix_tabliz),
    path('api/rayon/', RayonViewSetLV.as_view()),
    path('api/rayon/<int:pk>', RayonViewSetDV.as_view()),

    path('api/doctor/', DoctorViewSetLV.as_view()),
    path('api/doctor/<int:pk>', DoctorViewSetDV.as_view()),

    path('api/mkb10/', MKB10ViewSetLV.as_view()),
    path('api/mkb10/<int:pk>', MKB10ViewSetDV.as_view()),

    path('api/otchety/', OtchetyViewSetLV.as_view()),
    path('api/otchety/<int:pk>', OtchetyViewSetDV.as_view()),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),
    path('login', loginpage, name='login'),
    path('vhod', vhod, name='vhod'),
    path('vihod', vihod, name='vihod'),

    path('api2/beremennaya/', BeremennayaViewSetLV.as_view(), name='beremennaya_lv'),
    path('api2/beremennaya/<int:pk>', BeremennayaViewSetDV.as_view(), name='beremennaya_dv'),

    path('api2/anketa/<int:beremenya_id>/', AnketaViewSetLV.as_view(), name='anketa_lv'),
    path('api2/anketa/<int:beremenya_id>/<int:pk>', AnketaViewSetDV.as_view(), name='anketa_dv'),

    path('api2/napravlenie/<int:beremenya_id>/', NapravlenieViewSetLV.as_view(), name='napravlenie_lv'),
    path('api2/napravlenie/<int:beremenya_id>/<int:pk>', NapravlenieViewSetDV.as_view(), name='napravlenie_dv'),

    path('api2/konsultaciaya/<int:beremenya_id>/', KonsultaciayaViewSetLV.as_view(), name='konsultaciaya_lv'),
    path('api2/konsultaciaya/<int:beremenya_id>/<int:pk>', KonsultaciayaViewSetDV.as_view(), name='konsultaciaya_dv'),

    path('api2/novorojdenniy/<int:beremenya_id>/', NovorojdenniyViewSetLV.as_view(), name='novorojdenniy_lv'),
    path('api2/novorojdenniy/<int:beremenya_id>/<int:pk>', NovorojdenniyViewSetDV.as_view(), name='novorojdenniy_dv'),

    path('api2/smenaJK/<int:beremenya_id>/', SmenaJKViewSetLV.as_view(), name='smenaJK_lv'),
    path('api2/smenaJK/<int:beremenya_id>/<int:pk>', SmenaJKViewSetDV.as_view(), name='smenaJK_dv'),
]
