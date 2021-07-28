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


const RUS_LOCALIZ = {
    pagergotopagestring: "Страница",
    pagershowrowsstring: "Выводить по",
    pagerrangestring: " из ",
    pagernextbuttonstring: "Далее",
    pagerpreviousbuttonstring: "Назад",
    sortascendingstring: "От А до Я",
    sortdescendingstring: "От Я до А",
    sortremovestring: "Убрать сортировку",
    filterclearstring: "Очистить",
    filterstring: "Применить",
    filtershowrowstring: "Условия фильтрации:",
    filtershowrowdatestring: "Условия фильтрации:",
    filterorconditionstring: "Или",
    filterandconditionstring: "И",
    filterselectallstring: "(Все)",
    filterchoosestring: "Начните ввод...",

    filterstringcomparisonoperators: ['Пустой', 'Не пустой', 'Сожержит', 'Содержит с учетом регистра',
        'Не содержит', 'Не содержит с учетом регистра', 'Начинается', 'Начинается с учетом регистра',
        'Заканчивается', 'Заканчивается с учетом регистра', 'Равно', 'Равно с учетом регистра'],
    //
    // filterstringcomparisonoperators: ['empty', 'not empty', 'contains', 'contains(match case)',
    //     'Не содержит', 'does not contain(match case)', 'starts with', 'starts with(match case)',
    //     'ends with', 'ends with(match case)', 'equal', 'equal(match case)', 'null', 'not null'],


    filternumericcomparisonoperators: ['Равно', 'Не равно', 'Меньше', 'Меньше или равно', 'Больше', 'Больше или равно', 'Пустое', 'Не пустое'],
    filterdatecomparisonoperators: ['Равно', 'Не равно', 'Меньше', 'Меньше или равно', 'Больше', 'Больше или равно', 'Пустое', 'Не пустое'],
    filterbooleancomparisonoperators: ['Пустое', 'Не Пустое'],

    validationstring: "Не верный формат",
    emptydatastring: "Поиск не дал результата",
    filterselectstring: "Выбрать фильтр",
    loadtext: "Загрузка...",
    clearstring: "Очистить",
    todaystring: "Сегодня"
};

const URL_MEGA_JSON = './api/sbor_znachenii_spravocnix_tabliz/'
let MEGA_DANIE_SPRAVOCHNIX_TABLIZ;
let FLAG_ZAGRUZKI = false;


let get_mega_json = new Promise(function (resolve, reject) {
    fetch(URL_MEGA_JSON).then(function (response) {
        if (response.ok) {
            response.json().then(function (data) {
                resolve(data);
            }).catch(function () {
                alert('Не могу получить JSON справочные таблицы');
            })

        } else {
            alert('Не могу получить справочные таблицы');
        }
    })

});


// let mega_json = new Promise((resolve, reject) => {
//
//     setTimeout(() => {
//         // переведёт промис в состояние fulfilled с результатом "result"
//         resolve("result");
//     }, 1000);
//
//     timer = window.setInterval(function () {
//         if (FLAG_ZAGRUZKI === true) {
//             sourse = MEGA_DANIE_SPRAVOCHNIX_TABLIZ[nazvanie_tablizi].map(item => item.nazvanie)
//             clearInterval(timer);
//             resolve(re)
//         }
//     }, 1000);
//
// });


$(function () {


})


// //inputы
// $(document).ready(function () {
//     $(".input1").jqxInput({height: 23, width: 40, minLength: 1});
//     $(".input2").jqxInput({height: 23, width: 40, minLength: 1});
//     $(".input3").jqxInput({height: 23, width: 40, minLength: 1});
//     $(".input4").jqxInput({height: 23, width: 40, minLength: 1});
//     $(".input5").jqxInput({height: 23, width: 40, minLength: 1});
//     $(".input6").jqxInput({height: 23, width: 40, minLength: 1});
// });
//

//
// //галочка(чекбокс)
// $(document).ready(function () {
//     $('.acceptInput').jqxCheckBox({width: 'auto'});
// });
//
//
// //радиобаттоны
// $(document).ready(function () {
//     $(".jqxRadioButton").jqxRadioButton({width: 250, height: 25});
// });
//

// //выбор доктора
//
//
// $(document).ready(function () {
//     var source = [];
//     $(".jqxWidgetDropDoctor").jqxDropDownList({source: source, placeHolder: "Выбрать врача", width: 250, height: 30});
// });
//


function get_featxh_data(form) {
    let zapros_data = {};
    $.map(form.serializeArray(), function (n, i) {
        zapros_data[n['name']] = n['value'];
    });
    return JSON.stringify(zapros_data);
}



class Beremenya {
    URL = '/api/beremennaya/'
    HEADERS = {
    // "X-CSRFToken": getCookie("csrftoken"),
    "Accept": "application/json",
    "Content-Type": "application/json"
};


    create = async function (data) {
        console.log(data);
        let self = this;
        const response = await fetch(
            self.URL,
            {
                method: 'POST',
                body: data,
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    pareseFormToData($form) {
        console.log(get_featxh_data($form));
    }
}


$(function () {
    $('.novaya_beremennaya').submit(function (e) {
        e.preventDefault()
        let beremenya = new Beremenya();
        const data = beremenya.pareseFormToData($(this));
        beremenya.create(data);
    });
})

//
//
// async function save_beremennaya(url, data) {
//
//     let zapros = fetch(url, {
//         method: 'POST',
//         body: JSON.stringify(data),
//         headers: {
//             'Content-Type': 'application/json;charset=utf-8'
//         },
//     });
//     console.log('Статус ответа', zapros.status)
//     alert('Данные сохранены');
//      $('.tabliza_beremennaya').jqxGrid({source: $('.tabliza_beremennaya').jqxGrid('source')});
// }
//
//
// $(function () {
//     $('.novaya_beremennaya').submit(function (e) {
//
//
//         e.preventDefault();
//         let url = $(e.currentTarget).attr('action');
//         let data = $(e.currentTarget).serializeArray();
//         let data2 = {};
//         data.forEach(function (item, i, arr) {
//             data2[item['name']] = item['value'];
//         });
//
//         save_beremennaya(url, data2);
//
//     })
// });

