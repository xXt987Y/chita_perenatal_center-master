from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from apps.core.models import Doctor, MKB10, UrovenMedObsluzivaniya, Rayon, TipOrganizacii, MedOrganizacia, Roli, \
    Polzovateli, Autorecomendacii, StepenRiska, SemeynoePolojenie, Besplodie, MenstrualnayaFunkciya, \
    GeneticheskieFaktori, TipBesplodiya, NastuplenieBeremennostiVRezultate, ParitetBeremennosti, SamoproizvolniyAbort, \
    IskustvenniyAbort, OslojneniyaIskustvenniyAbort, OslojneniyaBeremennostiAnamez, KesarevoSechenie, SaharniyDiabed, \
    GestacionniySaharniyDiabed, ZabolevanieShitovidnoy, AKO, Koagulopatiya, FormaSujeniyaTaza, StepenSujeniyaTaza, \
    VzyataPodNabludenie, OslojneniyaRodov, Preeklampsiya, RezusSensibilizaciya, FetoplacentarnayaNedostatochnost, \
    NepravilnoePolojeniePloda, Mnogoplodie, PredlejaniePlacenti, UrovenPappa, UrovenBetaHgch, \
    NalichieVprPoRezultatamUzi, ObsheeSostoyaniePloda, MestoIshoda, GibelPloda, IshodBeremennosti, KesarevoSechenie1, \
    KesarevoSechenie2, KesarevoSechenie3, SmertNovorojdennogo, CelNapravleniya
from apps.core.serializers import DoctorSerializer, RayonSerializer


def home(request):
    return render(request, "home.html")


def sbor_znachenii_spravocnix_tabliz(request):

    rayon = Rayon.objects.all()
    uroven_med_obsluzivaniya = UrovenMedObsluzivaniya.objects.all()
    tip_organizacii = TipOrganizacii.objects.all()
    med_organizacia = MedOrganizacia.objects.all()
    # roli = Roli.objects.all()
    # polzovateli = Polzovateli.objects.all()
    doctor = Doctor.objects.all()
    mkb10 = MKB10.objects.all()
    # autorecomendacii = Autorecomendacii.objects.all()
    stepen_riska = StepenRiska.objects.all()
    semeynoe_polojenie = SemeynoePolojenie.objects.all()
    geneticheskie_faktori = GeneticheskieFaktori.objects.all()
    menstrualnaya_funkciya = MenstrualnayaFunkciya.objects.all()
    besplodie = Besplodie.objects.all()
    tip_besplodie = TipBesplodiya.objects.all()
    nastuplenie_beremennosti_v_rezultate = NastuplenieBeremennostiVRezultate.objects.all()
    paritet_beremennosti = ParitetBeremennosti.objects.all()
    samoproizvolniy_abort = SamoproizvolniyAbort.objects.all()
    iskustvenniy_abort = IskustvenniyAbort.objects.all()
    oslojneniya_iskustvenniy_abort = OslojneniyaIskustvenniyAbort.objects.all()
    oslojneniya_beremennosti_anamez = OslojneniyaBeremennostiAnamez.objects.all()
    kesarevo_sechenie = KesarevoSechenie.objects.all()
    saharniy_diabed = SaharniyDiabed.objects.all()
    gestacionniy_saharniy_diabed = GestacionniySaharniyDiabed.objects.all()
    zabolevanie_shitovidnoy = ZabolevanieShitovidnoy.objects.all()
    ako = AKO.objects.all()
    koagulopatiya = Koagulopatiya.objects.all()
    forma_sujeniya_taza = FormaSujeniyaTaza.objects.all()
    stepen_sujeniya_taza = StepenSujeniyaTaza.objects.all()
    vzyata_pod_nabludenie = VzyataPodNabludenie.objects.all()
    oslojneniya_rodov = OslojneniyaRodov.objects.all()
    preeklampsiya = Preeklampsiya.objects.all()
    rezus_sensibilizaciya = RezusSensibilizaciya.objects.all()
    fetoplacentarnaya_nedostatochnost = FetoplacentarnayaNedostatochnost.objects.all()

    nepravilnoe_polojenie_ploda = NepravilnoePolojeniePloda.objects.all()
    mnogoplodie = Mnogoplodie.objects.all()
    predlejanie_placenti = PredlejaniePlacenti.objects.all()
    uroven_pappa = UrovenPappa.objects.all()
    uroven_beta_hgch = UrovenBetaHgch.objects.all()
    nalichie_vpr_po_rezultatamUzi = NalichieVprPoRezultatamUzi.objects.all()
    obshee_sostoyanie_ploda = ObsheeSostoyaniePloda.objects.all()
    mesto_ishoda = MestoIshoda.objects.all()
    gibel_ploda = GibelPloda.objects.all()
    ishod_beremennosti = IshodBeremennosti.objects.all()
    kesarevo_sechenie1 = KesarevoSechenie1.objects.all()
    kesarevo_sechenie2 = KesarevoSechenie2.objects.all()
    kesarevo_sechenie3 = KesarevoSechenie3.objects.all()
    smert_novorojdennogo = SmertNovorojdennogo.objects.all()
    cel_napravleniya = CelNapravleniya.objects.all()

    data = {
        'rayon':RayonSerializer(rayon, many=True).data,
        # 'uroven_med_obsluzivaniya':uroven_med_obsluzivaniya,
        # 'tip_organizacii':tip_organizacii,
        # 'med_organizacia':med_organizacia,
        # 'doctor':doctor,
        # 'mkb10':mkb10,
        # 'stepen_riska':stepen_riska,
        # 'semeynoe_polojenie':semeynoe_polojenie,
        # 'geneticheskie_faktori':geneticheskie_faktori,
        # 'menstrualnaya_funkciya':menstrualnaya_funkciya,
        # 'besplodie':besplodie,
        # 'tip_besplodie':tip_besplodie,
        # 'nastuplenie_beremennosti_v_rezultate':nastuplenie_beremennosti_v_rezultate,
        # 'paritet_beremennosti':paritet_beremennosti,
        # 'samoproizvolniy_abort':samoproizvolniy_abort,
        # 'iskustvenniy_abort':iskustvenniy_abort,
        # 'oslojneniya_iskustvenniy_abort':oslojneniya_iskustvenniy_abort,
        # 'kesarevo_sechenie':kesarevo_sechenie,
        # 'saharniy_diabed':saharniy_diabed,
        # 'gestacionniy_saharniy_diabed':gestacionniy_saharniy_diabed,
        # 'zabolevanie_shitovidnoy':zabolevanie_shitovidnoy,
        # 'ako':ako,
        # 'koagulopatiya':koagulopatiya,
        # 'forma_sujeniya_taza':forma_sujeniya_taza,
        # 'stepen_sujeniya_taza':stepen_sujeniya_taza,
        # 'vzyata_pod_nabludenie':vzyata_pod_nabludenie,
        # 'oslojneniya_rodov':oslojneniya_rodov,
        # 'fetoplacentarnaya_nedostatochnost':fetoplacentarnaya_nedostatochnost,
        # 'preeklampsiya':preeklampsiya,
        # 'rezus_sensibilizaciya':rezus_sensibilizaciya,
        # 'nepravilnoe_polojenie_ploda':nepravilnoe_polojenie_ploda,
        # 'mnogoplodie':mnogoplodie,
        # 'predlejanie_placenti':predlejanie_placenti,
        # 'uroven_pappa':uroven_pappa,
        # 'uroven_beta_hgch':uroven_beta_hgch,
        # 'nalichie_vpr_po_rezultatamUzi':nalichie_vpr_po_rezultatamUzi,
        # 'obshee_sostoyanie_ploda':obshee_sostoyanie_ploda,
        # 'mesto_ishoda':mesto_ishoda,
        # 'gibel_ploda':gibel_ploda,
        # 'ishod_beremennosti':ishod_beremennosti,
        # 'kesarevo_sechenie1':kesarevo_sechenie1,
        # 'kesarevo_sechenie2':kesarevo_sechenie2,
        # 'kesarevo_sechenie3':kesarevo_sechenie3,
        # 'smert_novorojdennogo':smert_novorojdennogo,
        # 'cel_napravleniya':cel_napravleniya,
    }




    return JsonResponse(data)