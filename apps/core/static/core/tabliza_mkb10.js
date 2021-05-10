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


class TablizaMKB10 {

    constructor() {
        let self = this;
        this.$grid = $('#tabliza_mkb10');
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
            pagesize: 30,
        }
    }

    get fields() {
        return [
            {name: 'id', type: 'number'},
            // {name: 'data_zaivlenia', type: 'date'},
            {name: 'kod', type: 'string'},
            // {name: 'razmer_restruc', type: 'number'},
            {name: 'nazvanie', type: 'string'},

        ]
    }

    get colums() {
        return [
            {
                text: 'id',
                datafield: 'id',
                align: 'center',
                cellsalign: 'center',
                width: '5%'
            },

            {
                text: 'Код',
                datafield: 'kod',
                align: 'center',
                cellsalign: 'center',
                width: '40%',

            },


            {
                text: 'Название',
                datafield: 'nazvanie',
                align: 'center',
                cellsalign: 'center',
                width: '55%',

            },

        ];
    }

    get data_adapter() {

        return new $.jqx.dataAdapter({
            datatype: "json",
            data: 'data',
            url: '/api/mkb10/',
            datafields: this.fields,
            sortcolumn: 'id',
            sortdirection: 'desc'
        });
    }


}


$(document).ready(function () {
    new TablizaMKB10();

});