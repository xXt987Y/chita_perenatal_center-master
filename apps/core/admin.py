from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from apps.core.models import Rayon, UrovenMedObsluzivaniya, TipOrganizacii, MedOrganizacia, Polzovateli, Doctor, \
    MKB10, Autorecomendacii, StepenRiska, SemeynoePolojenie, GeneticheskieFaktori, MenstrualnayaFunkciya, Besplodie, \
    TipBesplodiya, NastuplenieBeremennostiVRezultate, ParitetBeremennosti, SamoproizvolniyAbort, IskustvenniyAbort, \
    OslojneniyaIskustvenniyAbort, OslojneniyaBeremennostiAnamez, KesarevoSechenie, SaharniyDiabed, \
    GestacionniySaharniyDiabed, \
    ZabolevanieShitovidnoy, AKO, Koagulopatiya, FormaSujeniyaTaza, StepenSujeniyaTaza, VzyataPodNabludenie, \
    OslojneniyaRodov, Beremennaya, Preeklampsiya, RezusSensibilizaciya, FetoplacentarnayaNedostatochnost, \
    NepravilnoePolojeniePloda, Mnogoplodie, PredlejaniePlacenti, UrovenPappa, UrovenBetaHgch, \
    NalichieVprPoRezultatamUzi, ObsheeSostoyaniePloda, Anketa, MestoIshoda, StepenRiskaPosleIshoda, GibelPloda, \
    IshodBeremennosti, KesarevoSechenie1, KesarevoSechenie2, KesarevoSechenie3, Ishod, SmertNovorojdennogo, \
    Novorojdenniy, CelNapravleniya, Napravlenie, Konsultaciaya, Smena_JK_u_beremennoy, VesaDliaOzenkiStepeniRiska


class RayonModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'nazvanie', 'korotkoe_nazvanie']
    list_filter = ['v_chite']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "nazvanie", "korotkoe_nazvanie", "v_chite"]

    class Meta:
        model = Rayon


admin.site.register(Rayon, RayonModelAdmin)


class UrovenMedObsluzivaniyaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = UrovenMedObsluzivaniya


admin.site.register(UrovenMedObsluzivaniya, UrovenMedObsluzivaniyaModelAdmin)






class TipOrganizaciiModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = TipOrganizacii


admin.site.register(TipOrganizacii, TipOrganizaciiModelAdmin)


class MedOrganizaciaModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'nazvanie', 'rayon__nazvanie']
    list_filter = ['tip_organizacii', 'uroven_med_obclujivaniya', 'ZKPC']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "nazvanie", "rayon", "tip_organizacii",
                    "uroven_med_obclujivaniya", "ZKPC",
                    "email", "kontaktnaya_informaciya", ]

    class Meta:
        model = MedOrganizacia


admin.site.register(MedOrganizacia, MedOrganizaciaModelAdmin)




class PolzovateliModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'user__username']
    list_filter = ['rol']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "user", "med_organiizaciya", "rol"]

    class Meta:
        model = Polzovateli


admin.site.register(Polzovateli, PolzovateliModelAdmin)


class DoctorModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'med_organiizaciya__nazvanie', 'fio']
    list_filter = ['rabotaet', 'med_organiizaciya']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "med_organiizaciya", "fio", "rabotaet", ]

    class Meta:
        model = Doctor


admin.site.register(Doctor, DoctorModelAdmin)


class MKB10ModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'kod', 'nazvanie']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "kod", "nazvanie"]

    class Meta:
        model = MKB10


admin.site.register(MKB10, MKB10ModelAdmin)


class AutorecomendaciiModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "code", "vozrastnaya_grupa", "recomendaciya", "use"]

    class Meta:
        model = Autorecomendacii


admin.site.register(Autorecomendacii, AutorecomendaciiModelAdmin)


class StepenRiskaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie", 'summa_vesov_ot', 'summa_vesov_do']
    list_editable = ['summa_vesov_ot', 'summa_vesov_do']

    class Meta:
        model = StepenRiska


admin.site.register(StepenRiska, StepenRiskaModelAdmin)


class SemeynoePolojenieModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = SemeynoePolojenie


admin.site.register(SemeynoePolojenie, SemeynoePolojenieModelAdmin)


class GeneticheskieFaktoriModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = GeneticheskieFaktori


admin.site.register(GeneticheskieFaktori, GeneticheskieFaktoriModelAdmin)


class MenstrualnayaFunkciyaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = MenstrualnayaFunkciya


admin.site.register(MenstrualnayaFunkciya, MenstrualnayaFunkciyaModelAdmin)


class BesplodieModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = Besplodie


admin.site.register(Besplodie, BesplodieModelAdmin)


class TipBesplodiyaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = TipBesplodiya


admin.site.register(TipBesplodiya, TipBesplodiyaModelAdmin)


class NastuplenieBeremennostiVRezultateModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = NastuplenieBeremennostiVRezultate


admin.site.register(NastuplenieBeremennostiVRezultate, NastuplenieBeremennostiVRezultateModelAdmin)


class ParitetBeremennostiModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = ParitetBeremennosti


admin.site.register(ParitetBeremennosti, ParitetBeremennostiModelAdmin)


class SamoproizvolniyAbortModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = SamoproizvolniyAbort


admin.site.register(SamoproizvolniyAbort, SamoproizvolniyAbortModelAdmin)


class IskustvenniyAbortModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = IskustvenniyAbort


admin.site.register(IskustvenniyAbort, IskustvenniyAbortModelAdmin)


class OslojneniyaIskustvenniyAbortModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = OslojneniyaIskustvenniyAbort


admin.site.register(OslojneniyaIskustvenniyAbort, OslojneniyaIskustvenniyAbortModelAdmin)


class OslojneniyaBeremennostiAnamezModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = OslojneniyaBeremennostiAnamez


admin.site.register(OslojneniyaBeremennostiAnamez, OslojneniyaBeremennostiAnamezModelAdmin)


class KesarevoSechenieModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = KesarevoSechenie


admin.site.register(KesarevoSechenie, KesarevoSechenieModelAdmin)


class SaharniyDiabedModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = SaharniyDiabed


admin.site.register(SaharniyDiabed, SaharniyDiabedModelAdmin)


class GestacionniySaharniyDiabedModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = GestacionniySaharniyDiabed


admin.site.register(GestacionniySaharniyDiabed, GestacionniySaharniyDiabedModelAdmin)


class ZabolevanieShitovidnoyModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = ZabolevanieShitovidnoy


admin.site.register(ZabolevanieShitovidnoy, ZabolevanieShitovidnoyModelAdmin)


class AKOModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = AKO


admin.site.register(AKO, AKOModelAdmin)


class KoagulopatiyaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = Koagulopatiya


admin.site.register(Koagulopatiya, KoagulopatiyaModelAdmin)


class FormaSujeniyaTazaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = FormaSujeniyaTaza


admin.site.register(FormaSujeniyaTaza, FormaSujeniyaTazaModelAdmin)


class StepenSujeniyaTazaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = StepenSujeniyaTaza


admin.site.register(StepenSujeniyaTaza, StepenSujeniyaTazaModelAdmin)


class VzyataPodNabludenieModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = VzyataPodNabludenie


admin.site.register(VzyataPodNabludenie, VzyataPodNabludenieModelAdmin)


class OslojneniyaRodovModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = OslojneniyaRodov


admin.site.register(OslojneniyaRodov, OslojneniyaRodovModelAdmin)


class BeremennayaModelAdmin(ImportExportModelAdmin):
    search_fields = ['jk_beremennoy__nazvanie', 'fio', 'nomer_telefona', 'nomer_oms', 'nomer', 'data_rojdeniya']
    list_filter = ['stepen_riska', 'data_vzyatiya', 'vozrast']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "jk_beremennoy", "nomer", "stepen_riska", "data_vzyatiya", "vrach", "fio", "data_rojdeniya",
                    "vozrast", "mesto_postoyannogo_projivaniya", "nomer_telefona", "nomer_oms"]

    class Meta:
        model = Beremennaya


admin.site.register(Beremennaya, BeremennayaModelAdmin)


class PreeklampsiyaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = Preeklampsiya


admin.site.register(Preeklampsiya, PreeklampsiyaModelAdmin)


class FetoplacentarnayaNedostatochnostModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = FetoplacentarnayaNedostatochnost


admin.site.register(FetoplacentarnayaNedostatochnost, FetoplacentarnayaNedostatochnostModelAdmin)


class RezusSensibilizaciyaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = RezusSensibilizaciya


admin.site.register(RezusSensibilizaciya, RezusSensibilizaciyaModelAdmin)


class NepravilnoePolojeniePlodaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = NepravilnoePolojeniePloda


admin.site.register(NepravilnoePolojeniePloda, NepravilnoePolojeniePlodaModelAdmin)


class MnogoplodieModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = Mnogoplodie


admin.site.register(Mnogoplodie, MnogoplodieModelAdmin)


class PredlejaniePlacentiModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = PredlejaniePlacenti


admin.site.register(PredlejaniePlacenti, PredlejaniePlacentiModelAdmin)


class UrovenPappaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = UrovenPappa


admin.site.register(UrovenPappa, UrovenPappaModelAdmin)


class UrovenBetaHgchModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = UrovenBetaHgch


admin.site.register(UrovenBetaHgch, UrovenBetaHgchModelAdmin)


class ObsheeSostoyaniePlodaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = ObsheeSostoyaniePloda


admin.site.register(ObsheeSostoyaniePloda, ObsheeSostoyaniePlodaModelAdmin)


class NalichieVprPoRezultatamUziModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = NalichieVprPoRezultatamUzi


admin.site.register(NalichieVprPoRezultatamUzi, NalichieVprPoRezultatamUziModelAdmin)


class AnketaModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'nomer_anketi__nomer', 'familiya_vracha__fio', 'nomer_protokola']
    list_filter = ['data_zapolneniya_anketi_vrachem', 'data_provedeniya_prenatalnogo_konsiliuma']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "nomer_anketi", "data_zapolneniya_anketi_vrachem", "familiya_vracha",
                    "data_provedeniya_prenatalnogo_konsiliuma", "nomer_protokola", "diagnoz_osnovnoy_mkb10"]

    class Meta:
        model = Anketa


admin.site.register(Anketa, AnketaModelAdmin)


class MestoIshodaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = MestoIshoda


admin.site.register(MestoIshoda, MestoIshodaModelAdmin)


class StepenRiskaPosleIshodaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = StepenRiskaPosleIshoda


admin.site.register(StepenRiskaPosleIshoda, StepenRiskaPosleIshodaModelAdmin)


class GibelPlodaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = GibelPloda


admin.site.register(GibelPloda, GibelPlodaModelAdmin)


class IshodBeremennostiModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = IshodBeremennosti


admin.site.register(IshodBeremennosti, IshodBeremennostiModelAdmin)


class KesarevoSechenie1ModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = KesarevoSechenie1


admin.site.register(KesarevoSechenie1, KesarevoSechenie1ModelAdmin)


class KesarevoSechenie2ModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = KesarevoSechenie2


admin.site.register(KesarevoSechenie2, KesarevoSechenie2ModelAdmin)


class KesarevoSechenie3ModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = KesarevoSechenie3


admin.site.register(KesarevoSechenie3, KesarevoSechenie3ModelAdmin)


class IshodModelAdmin(ImportExportModelAdmin):
    search_fields = ['id']
    list_filter = ['stepen_riska_posle_ishoda', 'data_ishoda', 'smert_materi', 'gibel_ploda']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "data_ishoda", "mesto_ishoda", "stepen_riska_posle_ishoda", "gibel_ploda",
                    "ishod_beremennosti", "smert_materi", "data_smerti_materi", "prichina_smerti_materi_mkb10"]

    class Meta:
        model = Ishod


admin.site.register(Ishod, IshodModelAdmin)


class SmertNovorojdennogoModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = SmertNovorojdennogo


admin.site.register(SmertNovorojdennogo, SmertNovorojdennogoModelAdmin)


class NovorojdenniyModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'nomer_beremennoy__nomer', 'nomer_novorojdennogo']
    list_filter = ['pol_novorojdennogo', 'ocenka_po_shkale_apgar_na1_min', 'ocenka_po_shkale_apgar_na5_min',
                   'smert_novorojdennogo']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "nomer_beremennoy", "nomer_novorojdennogo", "pol_novorojdennogo", "ves_novorojdennogo",
                    "rost_novorojdennogo", "ocenka_po_shkale_apgar_na1_min", "ocenka_po_shkale_apgar_na5_min",
                    "vpr_novorojdennogo_po_mkb10", "smert_novorojdennogo", "prichina_smerti_materi_po_mkb10"]

    class Meta:
        model = Novorojdenniy


admin.site.register(Novorojdenniy, NovorojdenniyModelAdmin)


class CelNapravleniyaModelAdmin(ImportExportModelAdmin):
    list_display = ["id", "nazvanie"]

    class Meta:
        model = CelNapravleniya


admin.site.register(CelNapravleniya, CelNapravleniyaModelAdmin)


class NapravlenieModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'nomer_beremennoy__nomer']
    list_filter = ['diagnoz_podtverjden', 'data', 'cel_napravleniya']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "nomer_beremennoy", "cel_napravleniya", "punkt_napravleniya", "predpolagaemyi_diagnoz",
                    "diagnoz_podtverjden", "data"]

    class Meta:
        model = Napravlenie


admin.site.register(Napravlenie, NapravlenieModelAdmin)


class KonsultaciayaModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'nomer_beremennoy__nomer', 'otpravitel__rol__nazvanie']
    list_filter = ['otpravleno']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "nomer_beremennoy", "otpravleno", "otpravitel", "tema", "soobshenie", "prochie"]

    class Meta:
        model = Konsultaciaya


admin.site.register(Konsultaciaya, KonsultaciayaModelAdmin)


class Smena_JK_u_beremennoyModelAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'nomer_beremennoy__nomer']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "nomer_beremennoy", "novaya_JK", "prichina"]

    class Meta:
        model = Smena_JK_u_beremennoy


admin.site.register(Smena_JK_u_beremennoy, Smena_JK_u_beremennoyModelAdmin)


class VesaDliaOzenkiStepeniRiskaAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'model_gde_smotret', 'stolbez_gde_smotret', 'znachenie', 'znachenie_chislo', 'znachenie_ot',
                     'znachenie_do', 'ozenka']
    list_filter = ['model_gde_smotret', 'stolbez_gde_smotret']
    list_display_links = ['id', 'model_gde_smotret']
    save_as_continue = True
    save_on_top = True
    save_as = True
    list_display = ["id", "model_gde_smotret", "stolbez_gde_smotret", "get_znachenie", 'ozenka']




admin.site.register(VesaDliaOzenkiStepeniRiska, VesaDliaOzenkiStepeniRiskaAdmin)
