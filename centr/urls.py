from django.contrib import admin
from django.urls import path, include

from scripts.ZagruzkaPolzovatelei import script_zagruzka_polzovatelei

urlpatterns = [
    path('',  include('apps.core.urls')),
    path('script_zagruzka_polzovatelei', script_zagruzka_polzovatelei),
    path('admin/', admin.site.urls),
]