const HEADERS = {
    "X-CSRFToken": getCookie("csrftoken"),
    "Accept": "application/json",
    "Content-Type": "application/json"
};

function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');

        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}


//ОТПРАВКА ФОРМЫ ВЫВОДА СРЕДСТВ
// $('.form-vivoda-sredstv').submit(async function (e) {
//     e.preventDefault();
//     let dataForm = new FormData(this);
//     const res = await fetch(URLS.api_zapros_vivoda_sredstv, {
//         method: 'POST',
//         headers: {'X-CSRFToken': getCookie('csrftoken')},
//         credentials: 'same-origin',
//         body: dataForm,
//         mode: 'same-origin'
//     });
//
//     if (!res.ok) { // код ответа не 200~
//         vivisti_uvedomlenie('Ошибка при отправки запроса', 'Попробуйте запрос чуть позже или обратитесь в поддержку', 'error')
//         throw new Error(`Не удалось получить ${URLS.api_zapros_vivoda_sredstv}, статус: ${res.status}`);
//     }
//
//     try {
//         res.json().then(function (resultJSON) {
//             vivisti_uvedomlenie(resultJSON['zagolovok'], resultJSON['telo'], 'success')
//         })
//
//     } catch (e) {
//         vivisti_uvedomlenie('Ошибка при отправки запроса', 'Попробуйте запрос чуть позже или обратитесь в поддержку', 'error')
//         throw new Error(`Не удалось распарсить ответ ${URLS.api_zapros_vivoda_sredstv}`);
//     }
//
// })


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


function get_featxh_data(form) {
    let zapros_data = {};
    $.map(form.serializeArray(), function (n, i) {
        if (n['value']) {
            zapros_data[n['name']] = n['value'];
        }

    });
    return JSON.stringify(zapros_data);
}


class Beremenya {
    URL = '/api/beremennaya/'
    HEADERS = {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    getList = async function (params) {
        const url = this.URl;
        Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
        const self = this;
        const response = await fetch(
            self.url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            return await response.json();
        } else {
            const text = await response.text();
        }
    }

    getDetail = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'get',
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

    create = async function (data) {
        let self = this;
        const response = await fetch(
            self.URL + 'post',
            {
                method: 'post',
                body: data,
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            alert('Добавление прошло успешно');
            $('.tabliza_beremennaya').jqxGrid({source: $('.tabliza_beremennaya').jqxGrid('source')});
            return await response.json();
        } else {
            const text = await response.text();
        }
    }

    update = async function (id, data) {
        const self = this;
        const url = `${self.URL}${id}`;

        const response = await fetch(
            url,
            {
                method: 'post',
                headers: self.HEADERS,
                body: data,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            alert('Изменение прошло успешно');
            $('.tabliza_beremennaya').jqxGrid({source: $('.tabliza_beremennaya').jqxGrid('source')});
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    delete = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'delete',
                headers: self.HEADERS,
                body: data,
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
        return get_featxh_data($form);
    }
}

$(function () {
    $('.novaya_beremennaya').submit(function (e) {
        e.preventDefault()
        let beremenya = new Beremenya();
        const data = beremenya.pareseFormToData($(this));
        if (BEREMENYA_ID) {
            beremenya.update(BEREMENYA_ID, data);
        } else {
            beremenya.create(data);
        }

    });
})

let BEREMENYA_ID = null;


class Anketa {
    URL = 'api/anketa/'
    HEADERS = {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    getList = async function (params) {
        const url = this.URl;
        Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
        const self = this;
        const response = await fetch(
            self.url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            return await response.json();
        } else {
            const text = await response.text();
        }
    }

    getDetail = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin",

            }
        )
        if (response.status === 200) {
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    create = async function (data) {
        let self = this;
        const response = await fetch(
            self.URL + 'post',
            {
                method: 'post',
                body: data,
                headers: self.HEADERS,
                credentials: 'same-origin',
                mode: 'same-origin'
            }
        )
        if (response.status === 200) {
            alert('Добавление прошло успешно');
            $('.tabliza_anketi').jqxGrid({source: $('.tabliza_anketi').jqxGrid('source')});
            return await response.json();
        } else {
            const text = await response.text();
        }
    }


    update = async function (id, data) {
        const self = this;
        const url = `${self.URL}${id}`;

        const response = await fetch(
            url,
            {
                method: 'post',
                headers: self.HEADERS,
                body: data,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            alert('Изменение прошло успешно');
            $('.tabliza_anketi').jqxGrid({source: $('.tabliza_anketi').jqxGrid('source')});
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    delete = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'delete',
                headers: self.HEADERS,
                body: data,
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
        return get_featxh_data($form);
    }
}

$(function () {
    $('.novaya_anketa').submit(function (e) {
        e.preventDefault()
        let anketa = new Anketa();
        const data = anketa.pareseFormToData($(this));
        if (ANKETA_ID) {
            anketa.update(ANKETA_ID, data);
        } else {
            anketa.create(data);
        }

    });
});

let ANKETA_ID = null;


class Napravlenie {
    URL = 'api/napravlenie/'
    HEADERS = {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    getList = async function (params) {
        const url = this.URl;
        Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
        const self = this;
        const response = await fetch(
            self.url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            return await response.json();
        } else {
            const text = await response.text();
        }
    }

    getDetail = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin",

            }
        )
        if (response.status === 200) {
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    create = async function (data) {
        let self = this;
        const response = await fetch(
            self.URL + 'post',
            {
                method: 'post',
                body: data,
                headers: self.HEADERS,
                credentials: 'same-origin',
                mode: 'same-origin'
            }
        )
        if (response.status === 200) {
            alert('Добавление прошло успешно');
            $('.tabliza_napravlenie').jqxGrid({source: $('.tabliza_napravlenie').jqxGrid('source')});
            return await response.json();
        } else {
            const text = await response.text();
        }
    }


    update = async function (id, data) {
        const self = this;
        const url = `${self.URL}${id}`;

        const response = await fetch(
            url,
            {
                method: 'post',
                headers: self.HEADERS,
                body: data,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            alert('Изменение прошло успешно');
            $('.tabliza_napravlenie').jqxGrid({source: $('.tabliza_napravlenie').jqxGrid('source')});
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    delete = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'delete',
                headers: self.HEADERS,
                body: data,
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
        return get_featxh_data($form);
    }
}

$(function () {
    $('.novoe_napravlenie').submit(function (e) {
        e.preventDefault()
        let napravlenie = new Napravlenie();
        const data = napravlenie.pareseFormToData($(this));
        if (NAPRAVLENIE_ID) {
            napravlenie.update(NAPRAVLENIE_ID, data);
        } else {
            napravlenie.create(data);
        }

    });
});

let NAPRAVLENIE_ID = null;


class Konsultaciaya {
    URL = 'api/konsultaciaya/'
    HEADERS = {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    getList = async function (params) {
        const url = this.URl;
        Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
        const self = this;
        const response = await fetch(
            self.url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            return await response.json();
        } else {
            const text = await response.text();
        }
    }

    getDetail = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin",

            }
        )
        if (response.status === 200) {
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    create = async function (data) {
        let self = this;
        const response = await fetch(
            self.URL + 'post',
            {
                method: 'post',
                body: data,
                headers: self.HEADERS,
                credentials: 'same-origin',
                mode: 'same-origin'
            }
        )
        if (response.status === 200) {

            alert('Добавление прошло успешно');
            $('.tabliza_konsultaciaya').jqxGrid({source: $('.tabliza_konsultaciaya').jqxGrid('source')});
            return await response.json();
        } else {
            const text = await response.text();
        }
    }


    update = async function (id, data) {
        const self = this;
        const url = `${self.URL}${id}`;

        const response = await fetch(
            url,
            {
                method: 'post',
                headers: self.HEADERS,
                body: data,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            alert('Изменение прошло успешно');
            $('.tabliza_konsultaciaya').jqxGrid({source: $('.tabliza_konsultaciaya').jqxGrid('source')});
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    delete = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'delete',
                headers: self.HEADERS,
                body: data,
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
        return get_featxh_data($form);
    }
}

$(function () {
    $('.novaya_konsultaciya').submit(function (e) {
        e.preventDefault()
        let konsultaciya = new Konsultaciaya();
        const data = konsultaciya.pareseFormToData($(this));
        if (KONSULTACIAYA_ID) {
            konsultaciya.update(KONSULTACIAYA_ID, data);
        } else {
            konsultaciya.create(data);
        }

    });
});

let KONSULTACIAYA_ID = null;

class SmenaJK {
    URL = 'api/smenaJK/'
    HEADERS = {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    getList = async function (params) {
        const url = this.URl;
        Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
        const self = this;
        const response = await fetch(
            self.url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            return await response.json();
        } else {
            const text = await response.text();
        }
    }

    getDetail = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin",

            }
        )
        if (response.status === 200) {
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    create = async function (data) {
        let self = this;
        const response = await fetch(
            self.URL + 'post',
            {
                method: 'post',
                body: data,
                headers: self.HEADERS,
                credentials: 'same-origin',
                mode: 'same-origin'
            }
        )
        if (response.status === 200) {

            alert('Добавление прошло успешно');
            return await response.json();
        } else {
            const text = await response.text();
        }
    }


    update = async function (id, data) {
        const self = this;
        const url = `${self.URL}${id}`;

        const response = await fetch(
            url,
            {
                method: 'post',
                headers: self.HEADERS,
                body: data,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            alert('Изменение прошло успешно');
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    delete = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'delete',
                headers: self.HEADERS,
                body: data,
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
        return get_featxh_data($form);
    }
}

$(function () {
    $('.smena_jk_u_beremennoy_form').submit(function (e) {
        e.preventDefault()
        let smenaJK = new SmenaJK();
        const data = smenaJK.pareseFormToData($(this));
        if (SmenaJK_ID) {
            smenaJK.update(SmenaJK_ID, data);
        } else {
            smenaJK.create(data);
        }

    });
});

let SmenaJK_ID = null;

class Novorojdenniy {
    URL = 'api/novorojdenniy/'
    HEADERS = {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    };

    getList = async function (params) {
        const url = this.URl;
        Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
        const self = this;
        const response = await fetch(
            self.url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            return await response.json();
        } else {
            const text = await response.text();
        }
    }

    getDetail = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'get',
                headers: self.HEADERS,
                credentials: "same-origin",

            }
        )
        if (response.status === 200) {
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    create = async function (data) {
        let self = this;
        const response = await fetch(
            self.URL + 'post',
            {
                method: 'post',
                body: data,
                headers: self.HEADERS,
                credentials: 'same-origin',
                mode: 'same-origin'
            }
        )
        if (response.status === 200) {
            alert('Добавление прошло успешно');
            $('.tabliza_novorojdenniy').jqxGrid({source: $('.tabliza_novorojdenniy').jqxGrid('source')});
            return await response.json();
        } else {
            const text = await response.text();
        }
    }


    update = async function (id, data) {
        const self = this;
        const url = `${self.URL}${id}`;

        const response = await fetch(
            url,
            {
                method: 'post',
                headers: self.HEADERS,
                body: data,
                credentials: "same-origin"
            }
        )
        if (response.status === 200) {
            alert('Изменение прошло успешно');
            $('.tabliza_novorojdenniy').jqxGrid({source: $('.tabliza_novorojdenniy').jqxGrid('source')});
            await response.json();
        } else {
            const text = await response.text();
        }
    }

    delete = async function (id) {
        const self = this;
        const url = `${self.URL}/${id}`;

        const response = await fetch(
            url,
            {
                method: 'delete',
                headers: self.HEADERS,
                body: data,
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
        return get_featxh_data($form);
    }
}

$(function () {
    $('.noviy_novorojdenniy').submit(function (e) {
        e.preventDefault()
        let novorojdenniy = new Novorojdenniy();
        const data = novorojdenniy.pareseFormToData($(this));
        if (NOVOROJDENNIY_ID) {
            novorojdenniy.update(NOVOROJDENNIY_ID, data);
        } else {
            novorojdenniy.create(data);
        }

    });
});

let NOVOROJDENNIY_ID = null;

$(".tabliza_beremennaya").on("filter", function (event) {
    // event arguments.
    var args = event.args;
    // page number.
    var pagenum = args.pagenum;
    // page size.
    var pagesize = args.pagesize;
    // sorting information.
    var sortInfo = event.args.sortinformation;
    var paginginformation = $(".tabliza_beremennaya").jqxGrid('getpaginginformation');
    var filterinfo = $(".tabliza_beremennaya").jqxGrid('getfilterinformation');
    let sbordannihstranici =
        [
            args.owner.pagesize,
            paginginformation.pagenum,
            args.owner.sortcolumn,
            args.owner.sortcolumns,
            args.owner.sortdirection,
            filterinfo,
        ]
    console.log(sbordannihstranici);
});

$(".tabliza_beremennaya").on("pagechanged", function (event) {
    // event arguments.
    var args = event.args;
    // page number.
    var pagenum = args.pagenum;
    // page size.
    var pagesize = args.pagesize;
    // sorting information.
    var sortInfo = event.args.sortinformation;
    var paginginformation = $(".tabliza_beremennaya").jqxGrid('getpaginginformation');
    var filterinfo = $(".tabliza_beremennaya").jqxGrid('getfilterinformation');
    let sbordannihstranici =
        [
            args.owner.pagesize,
            paginginformation.pagenum,
            args.owner.sortcolumn,
            args.owner.sortcolumns,
            args.owner.sortdirection,
            filterinfo,
        ]
    console.log(sbordannihstranici);
});

$(".tabliza_beremennaya").on("sort", function (event) {
    // event arguments.
    var args = event.args;
    console.log(event.args);
    // page number.
    var pagenum = args.pagenum;
    // page size.
    var pagesize = args.pagesize;
    // sorting information.
    var sortInfo = event.args.sortinformation;
    var paginginformation = $(".tabliza_beremennaya").jqxGrid('getpaginginformation');
    var filterinfo = $(".tabliza_beremennaya").jqxGrid('getfilterinformation');
    let sbordannihstranici =
        [
            args.owner.pagesize,
            paginginformation.pagenum,
            args.owner.sortcolumn,
            args.owner.sortcolumns,
            args.owner.sortdirection,
            filterinfo,
        ]
    let sbordannihstranicijson = JSON.stringify(sbordannihstranici);
    console.log(sbordannihstranici);
    console.log(sbordannihstranicijson);
    fetch(`/api/beremennaya/`).then(function (response) {
                    if (response.ok) {
                        response.json(sbordannihstranici);
                        // alert('1');
                    }
                    else {
                        alert('Не могу получить данные');
                    }
                });
});