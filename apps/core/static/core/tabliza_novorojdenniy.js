'use strict';

// Для преобразование инмпутов модели в объект
function objectifyForm(formArray) {//serialize data function
    let data = new FormData();
    for (let i = 0; i < formArray.length; i++) {
        data.append(formArray[i]['name'], formArray[i]['value']);
    }
    return data;
}

// Для коректной обработки статуса сервера
function checkStatus(res) {
    if (res.status >= 200 && res.status < 300) {
        return res
    } else {
        let err = new Error(res.statusText);
        err.response = res;
        console.error('Ошибка в адресе сервера', res);
        throw err
    }
}


class TablizaNovorojdenniy {

    constructor() {
        let self = this;
        this.$grid = $('#tabliza_novorojdenniy');
        this.$grid.jqxGrid(self.nastroiki_grida);
    }

    get nastroiki_grida() {
        let self = this;
        return {
            width: '100%',
            height: '100%',
            source: this.data_adapter,
            columns: this.colums,
            enabletooltips: true,
            // localization: RUS_LOCALIZ,
            filterable: true,
            showtoolbar: true,
            pageable: true,
            columnsresize: true,
            autorowheight: true,
            scrollmode: 'logical',
            rowsheight: 40,
            toolbarheight: 40,
            theme: 'light',
            altrows: true,
            sortable: true,
            showstatusbar: true,
            statusbarheight: 25,
            pagesizeoptions: ['5', '10', '30', '50', '100'],
            pagesize: 10,
        }
    }

    get fields() {
        return [
            {name: 'pol_novorojdennogo', type: 'string'},
            {name: 'ves_novorojdennogo', type: 'string'},
            {name: 'rost_novorojdennogo', type: 'string'},
            {name: 'ocenka_po_shkale_apgar_na1_min', type: 'string'},
            {name: 'ocenka_po_shkale_apgar_na5_min', type: 'string'},
            {name: 'vpr_novorojdennogo_po_mkb10', type: 'string'},
            {name: 'smert_novorojdennogo', type: 'string'},
        ]
    }

    get colums() {
        return [
            {
                text: 'Пол',
                datafield: 'pol_novorojdennogo',
                align: 'center',
                cellsalign: 'center',
                width: '200',

            },
            {
                text: 'Вес',
                datafield: 'ves_novorojdennogo',
                align: 'center',
                cellsalign: 'center',
                width: '200',

            },
            {
                text: 'Рост',
                datafield: 'rost_novorojdennogo',
                align: 'center',
                cellsalign: 'center',
                width: '200',

            },
            {
                text: 'Оценка по шкале АПГАР на 1 минуту',
                datafield: 'ocenka_po_shkale_apgar_na1_min',
                align: 'center',
                cellsalign: 'center',
                width: '200',

            },
            {
                text: 'Оценка по шкале АПГАР на 5 минут',
                datafield: 'ocenka_po_shkale_apgar_na5_min',
                align: 'center',
                cellsalign: 'center',
                width: '200',

            },
            {
                text: 'ВПР новорожденного (код по МКБ-10)',
                datafield: 'vpr_novorojdennogo_po_mkb10',
                align: 'center',
                cellsalign: 'center',
                width: '200',

            },
            {
                text: 'Смерть новорожденного',
                datafield: 'smert_novorojdennogo',
                align: 'center',
                cellsalign: 'center',
                width: '200',

            },
        ];
    }

    get data_adapter() {

        return new $.jqx.dataAdapter({
            datatype: "json",
            data: 'data',
            url: '/api/novorojdenniy/',
            datafields: this.fields,
            sortcolumn: 'id',
            sortdirection: 'desc'
        });
    }
}


$(document).ready(function () {
    new TablizaNovorojdenniy();

});