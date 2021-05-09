from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from apps.core.models import Rayon, UrovenMedObsluzivaniya, TipOrganizacii, MedOrganizacia, Roli, Polzovateli, Doctor, \
    MKB10, Autorecomendacii, StepenRiska, SemeynoePolojenie, GeneticheskieFaktori, MenstrualnayaFunkciya, Besplodie, \
    TipBesplodiya, NastuplenieBeremennostiVRezultate, ParitetBeremennosti, SamoproizvolniyAbort, IskustvenniyAbort, \
    OslojneniyaIskustvenniyAbort, OslojneniyaBeremennostiAnamez, KesarevoSechenie, SaharniyDiabed, \
    GestacionniySaharniyDiabed, \
    ZabolevanieShitovidnoy, AKO, Koagulopatiya, FormaSujeniyaTaza, StepenSujeniyaTaza, VzyataPodNabludenie, \
    OslojneniyaRodov, Beremennaya, Preeklampsiya, RezusSensibilizaciya, FetoplacentarnayaNedostatochnost, \
    NepravilnoePolojeniePloda, Mnogoplodie, PredlejaniePlacenti, UrovenPappa, UrovenBetaHgch, \
    NalichieVprPoRezultatamUzi, ObsheeSostoyaniePloda, Anketa, MestoIshoda, StepenRiskaPosleIshoda, GibelPloda, \
    IshodBeremennosti, KesarevoSechenie1, KesarevoSechenie2, KesarevoSechenie3, Ishod, SmertNovorojdennogo, \
    Novorojdenniy, CelNapravleniya, Napravlenie, Konsultaciaya, Smena_JK_u_beremennoy


class RayonModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie", "korotkoe_nazvanie", "v_chite"]

    class Meta:
        model = Rayon


admin.site.register(Rayon, RayonModelAdmin)


class UrovenMedObsluzivaniyaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = UrovenMedObsluzivaniya


admin.site.register(UrovenMedObsluzivaniya, UrovenMedObsluzivaniyaModelAdmin)


class TipOrganizaciiModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = TipOrganizacii


admin.site.register(TipOrganizacii, TipOrganizaciiModelAdmin)


class MedOrganizaciaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie", "rayon", "tip_organizacii",
                    "uroven_med_obclujivaniya", "ZKPC",
                    "email", "kontaktnaya_informaciya", ]

    class Meta:
        model = MedOrganizacia


admin.site.register(MedOrganizacia, MedOrganizaciaModelAdmin)


class RoliModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = Roli


admin.site.register(Roli, RoliModelAdmin)


class PolzovateliModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "user", "med_organiizaciya", "rol", ]

    class Meta:
        model = Polzovateli


admin.site.register(Polzovateli, PolzovateliModelAdmin)


class DoctorModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "med_organiizaciya", "fio", "rabotaet", ]

    class Meta:
        model = Doctor


admin.site.register(Doctor, DoctorModelAdmin)


class MKB10ModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "kod", "nazvanie"]

    class Meta:
        model = MKB10


admin.site.register(MKB10, MKB10ModelAdmin)


class AutorecomendaciiModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "code", "vozrastnaya_grupa", "recomendaciya", "use"]

    class Meta:
        model = Autorecomendacii


admin.site.register(Autorecomendacii, AutorecomendaciiModelAdmin)


class StepenRiskaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = StepenRiska


admin.site.register(StepenRiska, StepenRiskaModelAdmin)


class SemeynoePolojenieModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = SemeynoePolojenie


admin.site.register(SemeynoePolojenie, SemeynoePolojenieModelAdmin)


class GeneticheskieFaktoriModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = GeneticheskieFaktori


admin.site.register(GeneticheskieFaktori, GeneticheskieFaktoriModelAdmin)


class MenstrualnayaFunkciyaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = MenstrualnayaFunkciya


admin.site.register(MenstrualnayaFunkciya, MenstrualnayaFunkciyaModelAdmin)


class BesplodieModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = Besplodie


admin.site.register(Besplodie, BesplodieModelAdmin)


class TipBesplodiyaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = TipBesplodiya


admin.site.register(TipBesplodiya, TipBesplodiyaModelAdmin)


class NastuplenieBeremennostiVRezultateModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = NastuplenieBeremennostiVRezultate


admin.site.register(NastuplenieBeremennostiVRezultate, NastuplenieBeremennostiVRezultateModelAdmin)


class ParitetBeremennostiModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = ParitetBeremennosti


admin.site.register(ParitetBeremennosti, ParitetBeremennostiModelAdmin)


class SamoproizvolniyAbortModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = SamoproizvolniyAbort


admin.site.register(SamoproizvolniyAbort, SamoproizvolniyAbortModelAdmin)


class IskustvenniyAbortModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = IskustvenniyAbort


admin.site.register(IskustvenniyAbort, IskustvenniyAbortModelAdmin)


class OslojneniyaIskustvenniyAbortModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = OslojneniyaIskustvenniyAbort


admin.site.register(OslojneniyaIskustvenniyAbort, OslojneniyaIskustvenniyAbortModelAdmin)


class OslojneniyaBeremennostiAnamezModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = OslojneniyaBeremennostiAnamez


admin.site.register(OslojneniyaBeremennostiAnamez, OslojneniyaBeremennostiAnamezModelAdmin)


class KesarevoSechenieModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = KesarevoSechenie


admin.site.register(KesarevoSechenie, KesarevoSechenieModelAdmin)


class SaharniyDiabedModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = SaharniyDiabed


admin.site.register(SaharniyDiabed, SaharniyDiabedModelAdmin)


class GestacionniySaharniyDiabedModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = GestacionniySaharniyDiabed


admin.site.register(GestacionniySaharniyDiabed, GestacionniySaharniyDiabedModelAdmin)


class ZabolevanieShitovidnoyModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = ZabolevanieShitovidnoy


admin.site.register(ZabolevanieShitovidnoy, ZabolevanieShitovidnoyModelAdmin)


class AKOModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = AKO


admin.site.register(AKO, AKOModelAdmin)


class KoagulopatiyaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = Koagulopatiya


admin.site.register(Koagulopatiya, KoagulopatiyaModelAdmin)


class FormaSujeniyaTazaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = FormaSujeniyaTaza


admin.site.register(FormaSujeniyaTaza, FormaSujeniyaTazaModelAdmin)


class StepenSujeniyaTazaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = StepenSujeniyaTaza


admin.site.register(StepenSujeniyaTaza, StepenSujeniyaTazaModelAdmin)


class VzyataPodNabludenieModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = VzyataPodNabludenie


admin.site.register(VzyataPodNabludenie, VzyataPodNabludenieModelAdmin)


class OslojneniyaRodovModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = OslojneniyaRodov


admin.site.register(OslojneniyaRodov, OslojneniyaRodovModelAdmin)


class BeremennayaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nomer", "stepen_riska", "data_vzyatiya", "vrach", "fio", "data_rojdeniya", "vozrast",
                    "mesto_postoyannogo_projivaniya", "nomer_telefona", "nomer_oms", "vrednie_privichki_kurenie",
                    "vrednie_privichki_alco", "vrednie_privichki_narko", "vrednie_privichki_toxi",
                    "vrednie_factori_truda_himicheskie", "vrednie_factori_truda_radioactiv",
                    "vrednie_factori_truda_priem_lekarstvennih_sredstv", "vrednie_factori_truda_neudvl_jil_ysloviya",
                    "socialno_ugrojaemaya", "semeynoe_polojenie", "somaticheskie_pokazateli_muzskoy",
                    "somaticheskie_pokazateli_girsutizm", "ves", "rost", "index", "razmer_taza_ds", "razmer_taza_dc",
                    "razmer_taza_dt", "razmer_taza_cd",
                    "razmer_taza_ce", "razmer_taza_cv", "forma_sujeniya_taza", "stepen_sujeniya_taza",
                    "rezus_faktori_beremennoy_otca", "vzyata_pod_nabludenie", "geneticheskie_faktori",
                    "menstrualnaya_funkciya", "zabolevanie_vnut_pol_organov_vospalenie_neroj",
                    "zabolevanie_vnut_pol_organov_vospalenie_roj", "zabolevanie_vnut_pol_organov_opuhl",
                    "zabolevanie_vnut_pol_organov_mioma", "zabolevanie_vnut_pol_organov_gipoplaziya",
                    "zabolevanie_vnut_pol_organov_poroki", "zabolevanie_vnut_pol_organov_operacii_pred",
                    "zabolevanie_vnut_pol_organov_operacii_matk", "zabolevanie_vnut_pol_organov_istmiko",
                    "zabolevanie_vnut_pol_organov_onkologiya", "besplodie", "tip_besplodiya",
                    "nastuplenie_beremennosti_v_rezultate_eco", "nastuplenie_beremennosti_v_rezultate_ovulyacii",
                    "data_pervogo_dnya_posledney_menstruacii",
                    "paritet_beremennosti", "samoproizvolniy_abort", "vnematochnaya_beremennost",
                    "rezus_konfliktnaya_beremennost", "gemoliticheskaya_bolezn", "iskustvenniy_abort",
                    "iskustvenniy_abort_oslojneniya", "oslojneniya_beremennosti_anemez",
                    "oslojneniya_beremennosti_anemez_fetoplacent", "oslojneniya_beremennosti_anemez_obostrenie",
                    "oslojneniya_beremennosti_anemez_prejdevremennoy", "oslojneniya_rodov",
                    "oslojneniya_rodov_osl_razrivom", "oslojneniya_rodov_osl_krovotech", "oslojneniya_rodov_osl_gnoyno",
                    "oslojneniya_rodov_osl_mertvoroj", "kesarevo_sechenie",
                    "oslojneniya_anomaliyami_rodovoy_deyatelnosti", "klinicheski_uzkiy_taz",
                    "plodorazrushayushaya_operaciya", "novorojdenniy_plod_smert", "novorojdenniy_plod_ves",
                    "novorojdenniy_plod_nevrolgiych", "novorojdenniy_plod_vpr", "novorojdenniy_plod_perinatalnie",
                    "infekcionnie_bolezni_gripp", "infekcionnie_bolezni_sifilis", "infekcionnie_bolezni_vich",
                    "infekcionnie_bolezni_krasnuha", "infekcionnie_bolezni_orvi", "infekcionnie_bolezni_tuberkulez",
                    "infekcionnie_bolezni_virusniy_gepatit", "zlokachestvennie_obrazovaniya", "saharniy_diabed",
                    "gestacionniy_saharniy_diabed", "zabolevanie_shitovidnoy", "ako", "deincifalniy_sindrom",
                    "bolezni_krovi_anemiya", "bolezni_krovi_trombocitopeniya", "bolezni_krovi_trombozi",
                    "koagulopatiya", "psih_rastroystva_psihozi", "psih_rastroystva_narusheniya_lich",
                    "psih_rastroystva_shizofreniya", "psih_rastroystva_umstvennaya_otstalost",
                    "bolezni_nervnoy_sistemi_nasledstvennie", "bolezni_nervnoy_sistemi_vospalitelnie",
                    "bolezni_nervnoy_sistemi_miopiya"]

    class Meta:
        model = Beremennaya


admin.site.register(Beremennaya, BeremennayaModelAdmin)


class PreeklampsiyaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = Preeklampsiya


admin.site.register(Preeklampsiya, PreeklampsiyaModelAdmin)


class FetoplacentarnayaNedostatochnostModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = FetoplacentarnayaNedostatochnost


admin.site.register(FetoplacentarnayaNedostatochnost, FetoplacentarnayaNedostatochnostModelAdmin)


class RezusSensibilizaciyaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = RezusSensibilizaciya


admin.site.register(RezusSensibilizaciya, RezusSensibilizaciyaModelAdmin)


class NepravilnoePolojeniePlodaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = NepravilnoePolojeniePloda


admin.site.register(NepravilnoePolojeniePloda, NepravilnoePolojeniePlodaModelAdmin)


class MnogoplodieModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = Mnogoplodie


admin.site.register(Mnogoplodie, MnogoplodieModelAdmin)


class PredlejaniePlacentiModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = PredlejaniePlacenti


admin.site.register(PredlejaniePlacenti, PredlejaniePlacentiModelAdmin)


class UrovenPappaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = UrovenPappa


admin.site.register(UrovenPappa, UrovenPappaModelAdmin)


class UrovenBetaHgchModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = UrovenBetaHgch


admin.site.register(UrovenBetaHgch, UrovenBetaHgchModelAdmin)


class ObsheeSostoyaniePlodaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = ObsheeSostoyaniePloda


admin.site.register(ObsheeSostoyaniePloda, ObsheeSostoyaniePlodaModelAdmin)


class NalichieVprPoRezultatamUziModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = NalichieVprPoRezultatamUzi


admin.site.register(NalichieVprPoRezultatamUzi, NalichieVprPoRezultatamUziModelAdmin)


class AnketaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nomer_anketi", "data_zapolneniya_anketi_vrachem", "familiya_vracha", "ves_beremennoy",
                    "srok_beremennosti_po_obektivnim_dannim", "srok_beremennosti_po_dannim_uzi",
                    "srok_beremennosti_po_pervomu", "osobennosti_protekaniya_beremennosti_krovynistie",
                    "osobennosti_protekaniya_beremennosti_virazenniy_toxikoz",
                    "osobennosti_protekaniya_beremennosti_krovotechenie",
                    "ugroza_prerivaniya_do_22", "ugroza_prerivaniya_posle_22", "antifosfolipidniy_sindrom",
                    "preeklampsiya", "rezus_sensibilizaciya", "abo_sensibilizaciya",
                    "fetoplacentarnaya_nedostatochnost", "narushenie_okoplodnih_vod_mnogovodie",
                    "narushenie_okoplodnih_vod_malovodie", "narushenie_okoplodnih_vod_mekonialnie",
                    "nepravilnoe_polojenie_ploda", "obvitie_pupovini", "mnogoplodie", "krupniy_plod",
                    "predlejanie_placenti", "uroven_papp_a", "uroven_beta_hgch", "fakt_provedeniya_uzi_10_14",
                    "fakt_provedeniya_uzi_20_24",
                    "fakt_provedeniya_uzi_32_34", "fakt_provedeniya_uzi_32_34", "nesootvetstvie_dannih_uzi_soot",
                    "nesootvetstvie_dannih_uzi_fetomerii", "nesootvetstvie_dannih_uzi_placenti",
                    "nalichie_vpr_po_rezultatam_uzi",
                    "data_provedeniya_prenatalnogo_konsiliuma", "nomer_protokola", "obshee_sostoyanie_ploda",
                    "napravlena_na_extrennoe_rodorazreshenie", "diagnoz_osnovnoy_mkb10",
                    "dopolnitelnie_zamechaniya_vracha"]

    class Meta:
        model = Anketa


admin.site.register(Anketa, AnketaModelAdmin)


class MestoIshodaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = MestoIshoda


admin.site.register(MestoIshoda, MestoIshodaModelAdmin)


class StepenRiskaPosleIshodaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = StepenRiskaPosleIshoda


admin.site.register(StepenRiskaPosleIshoda, StepenRiskaPosleIshodaModelAdmin)


class GibelPlodaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = GibelPloda


admin.site.register(GibelPloda, GibelPlodaModelAdmin)


class IshodBeremennostiModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = IshodBeremennosti


admin.site.register(IshodBeremennosti, IshodBeremennostiModelAdmin)


class KesarevoSechenie1ModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = KesarevoSechenie1


admin.site.register(KesarevoSechenie1, KesarevoSechenie1ModelAdmin)


class KesarevoSechenie2ModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = KesarevoSechenie2


admin.site.register(KesarevoSechenie2, KesarevoSechenie2ModelAdmin)


class KesarevoSechenie3ModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = KesarevoSechenie3


admin.site.register(KesarevoSechenie3, KesarevoSechenie3ModelAdmin)


class IshodModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "data_ishoda", "mesto_ishoda", "stepen_riska_posle_ishoda", "gibel_ploda", "ishod_beremennosti",
                    "kesarevo_sechenie1", "kesarevo_sechenie2", "kesarevo_sechenie3", "preeklampsiya",
                    "predlejanie_placenti",
                    "prejdevrem_otsloyka", "anomalii_rodovoy_deyatelnosti", "klinicheski_uzkiy_taz", "razriv_matki",
                    "dvc_sindrom",
                    "emboliya", "smert_materi", "data_smerti_materi", "prichina_smerti_materi_mkb10"]

    class Meta:
        model = Ishod


admin.site.register(Ishod, IshodModelAdmin)


class SmertNovorojdennogoModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = SmertNovorojdennogo


admin.site.register(SmertNovorojdennogo, SmertNovorojdennogoModelAdmin)


class NovorojdenniyModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nomer_beremennoy", "nomer_novorojdennogo", "pol_novorojdennogo", "ves_novorojdennogo", "rost_novorojdennogo",
                    "ocenka_po_shkale_apgar_na1_min", "ocenka_po_shkale_apgar_na5_min",
                    "vpr_novorojdennogo_po_mkb10", "smert_novorojdennogo", "prichina_smerti_materi_po_mkb10"]

    class Meta:
        model = Novorojdenniy


admin.site.register(Novorojdenniy, NovorojdenniyModelAdmin)


class CelNapravleniyaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nazvanie"]

    class Meta:
        model = CelNapravleniya


admin.site.register(CelNapravleniya, CelNapravleniyaModelAdmin)


class NapravlenieModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nomer_beremennoy", "cel_napravleniya", "punkt_napravleniya", "predpolagaemyi_diagnoz", "diagnoz_podtverjden", "data"]

    class Meta:
        model = Napravlenie


admin.site.register(Napravlenie, NapravlenieModelAdmin)


class KonsultaciayaModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nomer_beremennoy", "otpravleno", "otpravitel", "tema", "soobshenie", "egp", "oaa",
                    "rubec_na_matke", "rh_sensibilizaciya", "prochie"]

    class Meta:
        model = Konsultaciaya


admin.site.register(Konsultaciaya, KonsultaciayaModelAdmin)


class Smena_JK_u_beremennoyModelAdmin(ImportExportModelAdmin):
    list_display = [ "id" , "nomer_beremennoy", "novaya_JK", "prichina"]

    class Meta:
        model = Smena_JK_u_beremennoy


admin.site.register(Smena_JK_u_beremennoy, Smena_JK_u_beremennoyModelAdmin)
