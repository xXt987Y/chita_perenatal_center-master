$(function () {
    $('.FIO_Poisk').jqxCheckBox({width: 'auto'});
    $('.NomerKarty_Poisk').jqxCheckBox({width: 'auto'});
    $('.GodOtkrKarty_Poisk').jqxCheckBox({width: 'auto'});
    $('.JKOtkrKarty_Poisk').jqxCheckBox({width: 'auto'});
    $('.OMS_Poisk').jqxCheckBox({width: 'auto'});
    $('.DataRojd_Poisk').jqxCheckBox({width: 'auto'});
    $('.DataPostNaUchet_Poisk').jqxCheckBox({width: 'auto'});
    $('.MestPostProj_Poisk').jqxCheckBox({width: 'auto'});
    $('.SrokTekBer_Poisk').jqxCheckBox({width: 'auto'});
    $('.SrokPoPoslAnk_Poisk').jqxCheckBox({width: 'auto'});
    $('.JKVedBer_Poisk').jqxCheckBox({width: 'auto'});
    $('.FIOUchVr_Poisk').jqxCheckBox({width: 'auto'});
    $('.IshodBer_Poisk').jqxCheckBox({width: 'auto'});
    $('.MestoIshoda_Poisk').jqxCheckBox({width: 'auto'});
    $('.StRiskaPosleIsh_Poisk').jqxCheckBox({width: 'auto'});
    $('.StRiskaBer_Poisk').jqxCheckBox({width: 'auto'});
    $(".OsnovBtn_Poisk").jqxToggleButton({toggled: false});
    $(".OsnovBtn_Poisk").on('click', function () {
        var toggled = $(".OsnovBtn_Poisk").jqxToggleButton('toggled');
    });
    $(".PokazBtn_Poisk").jqxToggleButton({toggled: false});
    $(".PokazBtn_Poisk").on('click', function () {
        var toggled = $(".PokazBtn_Poisk").jqxToggleButton('toggled');
    });
    $(".UbratBtn_Poisk").jqxToggleButton({toggled: false});
    $(".UbratBtn_Poisk").on('click', function () {
        var toggled = $(".UbratBtn_Poisk").jqxToggleButton('toggled');
    });
})