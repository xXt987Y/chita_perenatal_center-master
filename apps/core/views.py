from django.http import JsonResponse
from django.shortcuts import render

from apps.core.models import Doctor, MKB10, UrovenMedObsluzivaniya, Rayon, TipOrganizacii, MedOrganizacia, StepenRiska, \
    SemeynoePolojenie, Besplodie, MenstrualnayaFunkciya, \
    GeneticheskieFaktori, TipBesplodiya, NastuplenieBeremennostiVRezultate, ParitetBeremennosti, SamoproizvolniyAbort, \
    IskustvenniyAbort, OslojneniyaIskustvenniyAbort, OslojneniyaBeremennostiAnamez, KesarevoSechenie, SaharniyDiabed, \
    GestacionniySaharniyDiabed, ZabolevanieShitovidnoy, AKO, Koagulopatiya, FormaSujeniyaTaza, StepenSujeniyaTaza, \
    VzyataPodNabludenie, OslojneniyaRodov, Preeklampsiya, RezusSensibilizaciya, FetoplacentarnayaNedostatochnost, \
    NepravilnoePolojeniePloda, Mnogoplodie, PredlejaniePlacenti, UrovenPappa, UrovenBetaHgch, \
    NalichieVprPoRezultatamUzi, ObsheeSostoyaniePloda, MestoIshoda, GibelPloda, IshodBeremennosti, KesarevoSechenie1, \
    KesarevoSechenie2, KesarevoSechenie3, SmertNovorojdennogo, CelNapravleniya, StepenRiskaPosleIshoda
from apps.core.serializers import DoctorSerializer, RayonSerializer, UrovenMedObsluzivaniyaSerializer, \
    TipOrganizaciiSerializer, MedOrganizaciaSerializer, MKB10Serializer, StepenRiskaSerializer, \
    SemeynoePolojenieSerializer, GeneticheskieFaktoriSerializer, MenstrualnayaFunkciyaSerializer, BesplodieSerializer, \
    TipBesplodiyaSerializer, NastuplenieBeremennostiVRezultateSerializer, ParitetBeremennostiSerializer, \
    SamoproizvolniyAbortSerializer, IskustvenniyAbortSerializer, OslojneniyaIskustvenniyAbortSerializer, \
    KesarevoSechenieSerializer, SaharniyDiabedSerializer, GestacionniySaharniyDiabedSerializer, \
    ZabolevanieShitovidnoySerializer, AKOSerializer, KoagulopatiyaSerializer, FormaSujeniyaTazaSerializer, \
    StepenSujeniyaTazaSerializer, VzyataPodNabludenieSerializer, OslojneniyaRodovSerializer, PreeklampsiyaSerializer, \
    RezusSensibilizaciyaRodovSerializer, FetoplacentarnayaNedostatochnostSerializer, \
    NepravilnoePolojeniePlodaSerializer, MnogoplodieSerializer, PredlejaniePlacentiSerializer, UrovenPappaSerializer, \
    UrovenBetaHgchSerializer, NalichieVprPoRezultatamUziSerializer, MestoIshodaSerializer, \
    ObsheeSostoyaniePlodaSerializer, GibelPlodaSerializer, IshodBeremennostiPappaSerializer, \
    KesarevoSechenie1Serializer, KesarevoSechenie2Serializer, KesarevoSechenie3Serializer, \
    SmertNovorojdennogoSerializer, CelNapravleniyaSerializer, StepenRiskaPosleIshodaSerializer
from .forms import *


def home(request):
    form = BeremennayaFormPart1()
    beremennaya_vrednie_privichki_form = BeremennayaVredniePrivichki
    beremennaya_vrednie_factori_form = BeremennayaVrednieFactori(label_suffix='')
    beremennaya_form = BeremennayaForm
    beremennaya_infekcionnie_bolezni_form = BeremennayaInfekcionnieBolezniForm
    beremennaya_razmer_taza_form = BeremennayaRazmerTazaForm
    beremennaya_zabolevanie_vnut_form = BeremennayaZabolevanieVnutForm
    beremennayao_oslojneniya_beremennosti_form = BeremennayaOslojneniyaBeremennostiForm
    beremennayao_oslojneniya_rodov_form = BeremennayaOslojneniyaRodovForm
    beremennayao_novorojdenniy_plod_form = BeremennayaNovorojdenniyPlodForm
    beremennaya_bolezni_endokr_form = BeremennayaBolezniEndokrForm
    beremennaya_bolezni_krovi_form = BeremennayaBolezniKroviForm
    beremennaya_psih_rastroystva_form = BeremennayaPsihRastroystvaForm
    beremennaya_bolezni_ns_form = BeremennayaBolezniNsForm
    beremennaya_bolezni_sistemi_krovoob_form = BeremennayaBolezniSistemiKrovoobForm
    beremennaya_bolezni_organov_dihaniya_form = BeremennayaBolezniOrganovDihaniyaForm
    beremennaya_bolezni_organov_moch_form = BeremennayaBolezniOrganovMochForm
    anketa_form = AnketaForm()
    ishod_form = IshodForm()

    return render(request, "home.html", {
        'form': form,
        'anketa_form': anketa_form,
        'ishod_form': ishod_form,
        'beremennaya_vrednie_privichki_form': beremennaya_vrednie_privichki_form,
        'beremennaya_vrednie_factori_form': beremennaya_vrednie_factori_form,
        'beremennaya_form': beremennaya_form,
        'beremennaya_infekcionnie_bolezni_form': beremennaya_infekcionnie_bolezni_form,
        'beremennaya_razmer_taza_form': beremennaya_razmer_taza_form,
        'beremennaya_zabolevanie_vnut_form': beremennaya_zabolevanie_vnut_form,
        'beremennayao_oslojneniya_beremennosti_form': beremennayao_oslojneniya_beremennosti_form,
        'beremennayao_oslojneniya_rodov_form': beremennayao_oslojneniya_rodov_form,
        'beremennayao_novorojdenniy_plod_form': beremennayao_novorojdenniy_plod_form,
        'beremennaya_bolezni_endokr_form': beremennaya_bolezni_endokr_form,
        'beremennaya_bolezni_krovi_form': beremennaya_bolezni_krovi_form,
        'beremennaya_psih_rastroystva_form': beremennaya_psih_rastroystva_form,
        'beremennaya_bolezni_ns_form': beremennaya_bolezni_ns_form,
        'beremennaya_bolezni_sistemi_krovoob_form': beremennaya_bolezni_sistemi_krovoob_form,
        'beremennaya_bolezni_organov_dihaniya_form': beremennaya_bolezni_organov_dihaniya_form,
        'beremennaya_bolezni_organov_moch_form': beremennaya_bolezni_organov_moch_form,

    })



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
    stepen_riska_posle_ishoda = StepenRiskaPosleIshoda.objects.all()

    data = {
        'rayon': RayonSerializer(rayon, many=True).data,
        'uroven_med_obsluzivaniya': UrovenMedObsluzivaniyaSerializer(uroven_med_obsluzivaniya, many=True).data,
        'tip_organizacii': TipOrganizaciiSerializer(tip_organizacii, many=True).data,
        'med_organizacia': MedOrganizaciaSerializer(med_organizacia, many=True).data,
        'doctor': DoctorSerializer(doctor, many=True).data,
        'mkb10': MKB10Serializer(mkb10, many=True).data,
        'stepen_riska': StepenRiskaSerializer(stepen_riska, many=True).data,
        'semeynoe_polojenie': SemeynoePolojenieSerializer(semeynoe_polojenie, many=True).data,
        'geneticheskie_faktori': GeneticheskieFaktoriSerializer(geneticheskie_faktori, many=True).data,
        'menstrualnaya_funkciya': MenstrualnayaFunkciyaSerializer(menstrualnaya_funkciya, many=True).data,
        'besplodie': BesplodieSerializer(besplodie, many=True).data,
        'tip_besplodie': TipBesplodiyaSerializer(tip_besplodie, many=True).data,
        'nastuplenie_beremennosti_v_rezultate': NastuplenieBeremennostiVRezultateSerializer(
            nastuplenie_beremennosti_v_rezultate, many=True).data,
        'paritet_beremennosti': ParitetBeremennostiSerializer(paritet_beremennosti, many=True).data,
        'samoproizvolniy_abort': SamoproizvolniyAbortSerializer(samoproizvolniy_abort, many=True).data,
        'iskustvenniy_abort': IskustvenniyAbortSerializer(iskustvenniy_abort, many=True).data,
        'oslojneniya_iskustvenniy_abort': OslojneniyaIskustvenniyAbortSerializer(oslojneniya_iskustvenniy_abort,
                                                                                 many=True).data,
        'kesarevo_sechenie': KesarevoSechenieSerializer(kesarevo_sechenie, many=True).data,
        'saharniy_diabed': SaharniyDiabedSerializer(saharniy_diabed, many=True).data,
        'gestacionniy_saharniy_diabed': GestacionniySaharniyDiabedSerializer(gestacionniy_saharniy_diabed,
                                                                             many=True).data,
        'zabolevanie_shitovidnoy': ZabolevanieShitovidnoySerializer(zabolevanie_shitovidnoy, many=True).data,
        'ako': AKOSerializer(ako, many=True).data,
        'koagulopatiya': KoagulopatiyaSerializer(koagulopatiya, many=True).data,
        'forma_sujeniya_taza': FormaSujeniyaTazaSerializer(forma_sujeniya_taza, many=True).data,
        'stepen_sujeniya_taza': StepenSujeniyaTazaSerializer(stepen_sujeniya_taza, many=True).data,
        'vzyata_pod_nabludenie': VzyataPodNabludenieSerializer(vzyata_pod_nabludenie, many=True).data,
        'oslojneniya_rodov': OslojneniyaRodovSerializer(oslojneniya_rodov, many=True).data,
        'fetoplacentarnaya_nedostatochnost': PreeklampsiyaSerializer(fetoplacentarnaya_nedostatochnost, many=True).data,
        'preeklampsiya': RezusSensibilizaciyaRodovSerializer(preeklampsiya, many=True).data,
        'rezus_sensibilizaciya': FetoplacentarnayaNedostatochnostSerializer(rezus_sensibilizaciya, many=True).data,
        'nepravilnoe_polojenie_ploda': NepravilnoePolojeniePlodaSerializer(nepravilnoe_polojenie_ploda, many=True).data,
        'mnogoplodie': MnogoplodieSerializer(mnogoplodie, many=True).data,
        'predlejanie_placenti': PredlejaniePlacentiSerializer(predlejanie_placenti, many=True).data,
        'uroven_pappa': UrovenPappaSerializer(uroven_pappa, many=True).data,
        'uroven_beta_hgch': UrovenBetaHgchSerializer(uroven_beta_hgch, many=True).data,
        'nalichie_vpr_po_rezultatamUzi': NalichieVprPoRezultatamUziSerializer(nalichie_vpr_po_rezultatamUzi,
                                                                              many=True).data,
        'obshee_sostoyanie_ploda': ObsheeSostoyaniePlodaSerializer(obshee_sostoyanie_ploda, many=True).data,
        'mesto_ishoda': MestoIshodaSerializer(mesto_ishoda, many=True).data,
        'gibel_ploda': GibelPlodaSerializer(gibel_ploda, many=True).data,
        'ishod_beremennosti': IshodBeremennostiPappaSerializer(ishod_beremennosti, many=True).data,
        'kesarevo_sechenie1': KesarevoSechenie1Serializer(kesarevo_sechenie1, many=True).data,
        'kesarevo_sechenie2': KesarevoSechenie2Serializer(kesarevo_sechenie2, many=True).data,
        'kesarevo_sechenie3': KesarevoSechenie3Serializer(kesarevo_sechenie3, many=True).data,
        'smert_novorojdennogo': SmertNovorojdennogoSerializer(smert_novorojdennogo, many=True).data,
        'cel_napravleniya': CelNapravleniyaSerializer(cel_napravleniya, many=True).data,
        'stepen_riska_posle_ishoda': StepenRiskaPosleIshodaSerializer(stepen_riska_posle_ishoda, many=True).data,
    }

    return JsonResponse(data)
