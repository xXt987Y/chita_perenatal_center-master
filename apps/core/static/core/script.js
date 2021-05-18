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

    filterstringcomparisonoperators: ['Пустой', 'Не пустой', 'contains', 'Содержит с учетом регистра',
        'Не содержит', 'Не содержит с учетом регистра', 'Начинается', 'Начинается с учетом регистра',
        'Заканчивается', 'Заканчивается с учетом регистра', 'Равно', 'Равно с учетом регистра', 'null', 'not null'],
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


async function get_mega_json() {
    let response = await fetch(URL_MEGA_JSON);
    if (response.ok) {
        let data = await response.json();
        MEGA_DANIE_SPRAVOCHNIX_TABLIZ = data;
        FLAG_ZAGRUZKI = true;
        console.log(MEGA_DANIE_SPRAVOCHNIX_TABLIZ);
    } else {
        alert('Не могу получить справочные таблицы');
    }
}


$(async function () {
    await get_mega_json();

});

$(function () {
    timer = window.setInterval(function () {
        if (FLAG_ZAGRUZKI === true) {
            let source = [
                "Нет",
                "Есть"
            ];
            // Create a jqxComboBox
            console.log('Было', source);
            sourse = MEGA_DANIE_SPRAVOCHNIX_TABLIZ['tip_besplodie'].map(item => item.nazvanie)
            console.log('Станет', sourse);
            clearInterval(timer);
        }
    }, 1000);


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
