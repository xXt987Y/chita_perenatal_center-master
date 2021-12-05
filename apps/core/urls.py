from django.urls import path

# router = routers.DefaultRouter()
# router.register(r'rayon', RayonViewSet)
from apps.core.api import RayonViewSetLV, RayonViewSetDV, BeremennayaViewSetLV, BeremennayaViewSetDV, DoctorViewSetLV, \
    DoctorViewSetDV, NovorojdenniyViewSetLV, NovorojdenniyViewSetDV, NapravlenieViewSetLV, NapravlenieViewSetDV, \
    KonsultaciayaViewSetLV, KonsultaciayaViewSetDV, MKB10ViewSetLV, MKB10ViewSetDV, SmenaJKViewSetLV, SmenaJKViewSetDV, \
    AnketaViewSetLV, AnketaViewSetDV, BeremennayaViewSetLV2, AnketaViewSetLV2, NapravlenieViewSetLV2, \
    KonsultaciayaViewSetLV2, SmenaJKViewSetLV2, NovorojdenniyViewSetLV2, OtchetyViewSetLV, OtchetyViewSetDV, \
    KonsultaciayaViewSetDV2, NapravlenieViewSetDV2
from apps.core.views import home, sbor_znachenii_spravocnix_tabliz, vhod, vihod, loginpage

urlpatterns = [
    path('api/sbor_znachenii_spravocnix_tabliz/', sbor_znachenii_spravocnix_tabliz),
    path('api/rayon/', RayonViewSetLV.as_view()),
    path('api/rayon/<int:pk>', RayonViewSetDV.as_view()),
    path('api/beremennaya/post', BeremennayaViewSetLV2.as_view(), name='beremennaya_lv_post'),
    path('api/beremennaya/', BeremennayaViewSetLV.as_view(), name='beremennaya_lv'),
    path('api/beremennaya/<int:pk>', BeremennayaViewSetDV.as_view(), name='beremennaya_dv'),
    path('api/doctor/', DoctorViewSetLV.as_view()),
    path('api/doctor/<int:pk>', DoctorViewSetDV.as_view()),
    path('api/novorojdenniy/post', NovorojdenniyViewSetLV2.as_view(), name='novorojdenniy_lv_post'),
    path('api/novorojdenniy/', NovorojdenniyViewSetLV.as_view(), name='novorojdenniy_lv'),
    path('api/novorojdenniy/<int:pk>', NovorojdenniyViewSetDV.as_view(), name='novorojdenniy_dv'),
    path('api/napravlenie/post', NapravlenieViewSetLV2.as_view(), name='napravlenie_lv_post'),
    path('api/napravlenie/', NapravlenieViewSetLV.as_view(), name='napravlenie_lv'),
    path('api/napravlenie/<int:pk>', NapravlenieViewSetDV.as_view(), name='napravlenie_dv'),
    path('api/napravlenie/napr/<int:pk>', NapravlenieViewSetDV2.as_view(), name='napravlenie_dv2'),
    path('api/konsultaciaya/post', KonsultaciayaViewSetLV2.as_view(), name='konsultaciaya_lv_post'),
    path('api/konsultaciaya/', KonsultaciayaViewSetLV.as_view(), name='konsultaciaya_lv'),
    path('api/konsultaciaya/<int:pk>', KonsultaciayaViewSetDV.as_view(), name='konsultaciaya_dv'),
    path('api/konsultaciaya/kons/<int:pk>', KonsultaciayaViewSetDV2.as_view(), name='konsultaciaya_dv2'),
    path('api/mkb10/', MKB10ViewSetLV.as_view()),
    path('api/mkb10/<int:pk>', MKB10ViewSetDV.as_view()),
    path('api/smenaJK/post', SmenaJKViewSetLV2.as_view(), name='smenaJK_lv_post'),
    path('api/smenaJK/', SmenaJKViewSetLV.as_view(), name='smenaJK_lv'),
    path('api/smenaJK/<int:pk>', SmenaJKViewSetDV.as_view(), name='smenaJK_dv'),
    path('api/anketa/post', AnketaViewSetLV2.as_view(), name='anketa_lv_post'),
    path('api/anketa/', AnketaViewSetLV.as_view(), name='anketa_lv'),
    path('api/anketa/<int:pk>', AnketaViewSetDV.as_view(), name='anketa_dv'),
    path('api/otchety/', OtchetyViewSetLV.as_view()),
    path('api/otchety/<int:pk>', OtchetyViewSetDV.as_view()),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),
    path('login', loginpage, name='login'),
    path('vhod', vhod, name='vhod'),
    path('vihod', vihod, name='vihod'),

]
