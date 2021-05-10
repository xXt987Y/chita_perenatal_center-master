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


class TablizaKonsultaciaya {

    constructor() {
        let self = this;
        this.$grid = $('#tabliza_smenaJK');
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
            theme: 'arctic',
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
            {name: 'id', type: 'number'},
            {name: 'nomer_beremennoy_title', type: 'data'},
            {name: 'prichina', type: 'string'},
            {name: 'med_organiizaciya_title', type: 'string'},
        ]
    }

    get colums() {
        return [
            {
                text: 'ID',
                datafield: 'id',
                align: 'center',
                cellsalign: 'center',
                width: '10%',

            },
            {
                text: 'ФИО беременной',
                datafield: 'nomer_beremennoy_title',
                align: 'center',
                cellsalign: 'center',
                width: '30%',

            },
            {
                text: 'Причина перевода',
                datafield: 'prichina',
                align: 'center',
                cellsalign: 'center',
                width: '30%',

            },
            {
                text: 'Новая ЖК',
                datafield: 'med_organiizaciya_title',
                align: 'center',
                cellsalign: 'center',
                width: '30%',

            },

        ];
    }

    get data_adapter() {

        return new $.jqx.dataAdapter({
            datatype: "json",
            data: 'data',
            url: '/api/smenaJK/',
            datafields: this.fields,
            sortcolumn: 'id',
            sortdirection: 'desc'
        });
    }
}


$(document).ready(function () {
    new TablizaKonsultaciaya();

});