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
function get_mega_json() {
    fetch(URL_MEGA_JSON).then(function (response) {
        response.json().then(function (data) {
            MEGA_DANIE_SPRAVOCHNIX_TABLIZ = data;
            console.log(MEGA_DANIE_SPRAVOCHNIX_TABLIZ);
        })
    });
}


$(function (){
    get_mega_json();
});

//
//
// //Кнопки для меню
// $(document).ready(function () {
//     $(".jqxButton1").jqxToggleButton({toggled: false});
//     $(".jqxButton1").on('click', function () {
//         var toggled = $(".jqxButton1").jqxToggleButton('toggled');
//         $('#pole').show();
//         $('#poisk').hide();
//     });
//     //КНОПКА ПОИСКА
//     $(".jqxButton21").jqxToggleButton({toggled: false});
//     $(".jqxButton21").on('click', function () {
//         var toggled = $(".jqxButton21").jqxToggleButton('toggled');
//         $('#pole').hide();
//         $('#poisk').show();
//     });
//     $(".jqxButton4").jqxToggleButton({toggled: false});
//     $(".jqxButton4").on('click', function () {
//         var toggled = $(".jqxButton4").jqxToggleButton('toggled');
//     });
//     $(".jqxButton5").jqxToggleButton({toggled: false});
//     $(".jqxButton5").on('click', function () {
//         var toggled = $(".jqxButton5").jqxToggleButton('toggled');
//     });
//     $(".jqxButton6").jqxToggleButton({toggled: false});
//     $(".jqxButton6").on('click', function () {
//         var toggled = $(".jqxButton6").jqxToggleButton('toggled');
//     });
//     $(".jqxButton17").jqxToggleButton({toggled: false});
//     $(".jqxButton17").on('click', function () {
//         var toggled = $(".jqxButton17").jqxToggleButton('toggled');
//     });
//     $(".jqxButton8").jqxToggleButton({toggled: false});
//     $(".jqxButton8").on('click', function () {
//         var toggled = $(".jqxButton8").jqxToggleButton('toggled');
//     });
//     $(".jqxButton9").jqxToggleButton({toggled: false});
//     $(".jqxButton9").on('click', function () {
//         var toggled = $(".jqxButton9").jqxToggleButton('toggled');
//     });
//     $(".jqxButton10").jqxToggleButton({toggled: false});
//     $(".jqxButton10").on('click', function () {
//         var toggled = $(".jqxButton10").jqxToggleButton('toggled');
//     });
//     $(".jqxButton11").jqxToggleButton({toggled: false});
//     $(".jqxButton11").on('click', function () {
//         var toggled = $(".jqxButton11").jqxToggleButton('toggled');
//     });
//     $(".jqxButton12").jqxToggleButton({toggled: false});
//     $(".jqxButton12").on('click', function () {
//         var toggled = $(".jqxButton12").jqxToggleButton('toggled');
//     });
//     $(".jqxButton13").jqxToggleButton({toggled: false});
//     $(".jqxButton13").on('click', function () {
//         var toggled = $(".jqxButton13").jqxToggleButton('toggled');
//     });
//     $(".jqxButton14").jqxToggleButton({toggled: false});
//     $(".jqxButton14").on('click', function () {
//         var toggled = $(".jqxButton14").jqxToggleButton('toggled');
//     });
//     $(".jqxButton15").jqxToggleButton({toggled: false});
//     $(".jqxButton15").on('click', function () {
//         var toggled = $(".jqxButton15").jqxToggleButton('toggled');
//     });
//     $(".jqxButton16").jqxToggleButton({toggled: false});
//     $(".jqxButton16").on('click', function () {
//         var toggled = $(".jqxButton16").jqxToggleButton('toggled');
//     });
//     $(".jqxButton18").jqxToggleButton({toggled: false});
//     $(".jqxButton18").on('click', function () {
//         var toggled = $(".jqxButton18").jqxToggleButton('toggled');
//     });
//     $(".jqxButtonNovoeNapravlenie").jqxToggleButton({toggled: false});
//     $(".jqxButtonNovoeNapravlenie").on('click', function () {
//         var toggled = $(".jqxButtonNovoeNapravlenie").jqxToggleButton('toggled');
//     });
//     $(".jqxButtonYdalitNapravlenie").jqxToggleButton({toggled: false});
//     $(".jqxButtonYdalitNapravlenie").on('click', function () {
//         var toggled = $(".jqxButtonYdalitNapravlenie").jqxToggleButton('toggled');
//     });
//
// });
//
// //Дата
// $(document).ready(function () {
//     $(".jqxDateTimeInput").jqxDateTimeInput({width: '125px', height: '25px'});
// });
//
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
// //комбобокс
// $(document).ready(function () {
//     var source = [
//         "Нет",
//         "Есть"
//     ];
//     // Create a jqxComboBox
//     $(".jqxComboBox").jqxComboBox({selectedIndex: 1, source: source, width: '200px', height: '30px'});
// });
//
// //галочка(чекбокс)
// $(document).ready(function () {
//     $('.acceptInput').jqxCheckBox({width: 'auto'});
// });
//
// //номер телефона
// $(document).ready(function () {
//     // Create jqxMaskedInput
//     $(".numericInput").jqxMaskedInput({width: '250px', height: '25px', mask: '#(###)###-##-##'});
//
// });
// $(document).ready(function () {
//     $(".ds").on("input", function () {
//         $(".in_ds").val(this.value);
//     });
// });
//
// //радиобаттоны
// $(document).ready(function () {
//     $(".jqxRadioButton").jqxRadioButton({width: 250, height: 25});
// });
//
// //ползунок ds
// $(document).ready(function () {
//     const num = document.getElementById('numds');
//     const rng = document.getElementById('rangeds');
//     const view = document.getElementById('viewds');
//     const goods = document.querySelectorAll('.good');
//     const set = val => {
//         num.value = val;
//         rng.value = val;
//         view.textContent = val;
//         [...goods].forEach(good => {
//             const options = good.querySelectorAll('.option');
//             [...options].forEach(option => {
//                 option.style.display = val >= +option.dataset.from ? 'block' : 'none';
//             });
//         });
//     }
//     rng.addEventListener('input', () => set(rng.value));
//     num.addEventListener('change', () => set(num.value));
// });
// //ползунок dc
// $(document).ready(function () {
//     const num = document.getElementById('numdc');
//     const rng = document.getElementById('rangedc');
//     const view = document.getElementById('viewdc');
//     const goods = document.querySelectorAll('.good');
//     const set = val => {
//         num.value = val;
//         rng.value = val;
//         view.textContent = val;
//         [...goods].forEach(good => {
//             const options = good.querySelectorAll('.option');
//             [...options].forEach(option => {
//                 option.style.display = val >= +option.dataset.from ? 'block' : 'none';
//             });
//         });
//     }
//     rng.addEventListener('input', () => set(rng.value));
//     num.addEventListener('change', () => set(num.value));
// });
// //ползунок dt
// $(document).ready(function () {
//     const num = document.getElementById('numdt');
//     const rng = document.getElementById('rangedt');
//     const view = document.getElementById('viewdt');
//     const goods = document.querySelectorAll('.good');
//     const set = val => {
//         num.value = val;
//         rng.value = val;
//         view.textContent = val;
//         [...goods].forEach(good => {
//             const options = good.querySelectorAll('.option');
//             [...options].forEach(option => {
//                 option.style.display = val >= +option.dataset.from ? 'block' : 'none';
//             });
//         });
//     }
//     rng.addEventListener('input', () => set(rng.value));
//     num.addEventListener('change', () => set(num.value));
// });
// //ползунок cd
// $(document).ready(function () {
//     const num = document.getElementById('numcd');
//     const rng = document.getElementById('rangecd');
//     const view = document.getElementById('viewcd');
//     const goods = document.querySelectorAll('.good');
//     const set = val => {
//         num.value = val;
//         rng.value = val;
//         view.textContent = val;
//         [...goods].forEach(good => {
//             const options = good.querySelectorAll('.option');
//             [...options].forEach(option => {
//                 option.style.display = val >= +option.dataset.from ? 'block' : 'none';
//             });
//         });
//     }
//     rng.addEventListener('input', () => set(rng.value));
//     num.addEventListener('change', () => set(num.value));
// });
// //ползунок ce
// $(document).ready(function () {
//     const num = document.getElementById('numce');
//     const rng = document.getElementById('rangece');
//     const view = document.getElementById('viewce');
//     const goods = document.querySelectorAll('.good');
//     const set = val => {
//         num.value = val;
//         rng.value = val;
//         view.textContent = val;
//         [...goods].forEach(good => {
//             const options = good.querySelectorAll('.option');
//             [...options].forEach(option => {
//                 option.style.display = val >= +option.dataset.from ? 'block' : 'none';
//             });
//         });
//     }
//     rng.addEventListener('input', () => set(rng.value));
//     num.addEventListener('change', () => set(num.value));
// });
// //ползунок cv
// $(document).ready(function () {
//     const num = document.getElementById('numcv');
//     const rng = document.getElementById('rangecv');
//     const view = document.getElementById('viewcv');
//     const goods = document.querySelectorAll('.good');
//     const set = val => {
//         num.value = val;
//         rng.value = val;
//         view.textContent = val;
//         [...goods].forEach(good => {
//             const options = good.querySelectorAll('.option');
//             [...options].forEach(option => {
//                 option.style.display = val >= +option.dataset.from ? 'block' : 'none';
//             });
//         });
//     }
//     rng.addEventListener('input', () => set(rng.value));
//     num.addEventListener('change', () => set(num.value));
// });
//
//
// $(function () {
//     //Всплывающее окно Window
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
