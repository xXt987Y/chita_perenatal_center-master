//Кнопки для меню
$(document).ready(function () {
    $(".jqxButton1").jqxToggleButton({toggled: false});
    $(".jqxButton1").on('click', function () {
        var toggled = $(".jqxButton1").jqxToggleButton('toggled');
    });
    $(".jqxButton2").jqxToggleButton({toggled: false});
    $(".jqxButton2").on('click', function () {
        var toggled = $(".jqxButton2").jqxToggleButton('toggled');
    });
    $(".jqxButton4").jqxToggleButton({toggled: false});
    $(".jqxButton4").on('click', function () {
        var toggled = $(".jqxButton4").jqxToggleButton('toggled');
    });
    $(".jqxButton5").jqxToggleButton({toggled: false});
    $(".jqxButton5").on('click', function () {
        var toggled = $(".jqxButton5").jqxToggleButton('toggled');
    });
    $(".jqxButton6").jqxToggleButton({toggled: false});
    $(".jqxButton6").on('click', function () {
        var toggled = $(".jqxButton6").jqxToggleButton('toggled');
    });
    $(".jqxButton7").jqxToggleButton({toggled: false});
    $(".jqxButton7").on('click', function () {
        var toggled = $(".jqxButton7").jqxToggleButton('toggled');
    });
    $(".jqxButton8").jqxToggleButton({toggled: false});
    $(".jqxButton8").on('click', function () {
        var toggled = $(".jqxButton8").jqxToggleButton('toggled');
    });
    $(".jqxButton9").jqxToggleButton({toggled: false});
    $(".jqxButton9").on('click', function () {
        var toggled = $(".jqxButton9").jqxToggleButton('toggled');
    });
    $(".jqxButton10").jqxToggleButton({toggled: false});
    $(".jqxButton10").on('click', function () {
        var toggled = $(".jqxButton10").jqxToggleButton('toggled');
    });
    $(".jqxButton11").jqxToggleButton({toggled: false});
    $(".jqxButton11").on('click', function () {
        var toggled = $(".jqxButton11").jqxToggleButton('toggled');
    });
    $(".jqxButton12").jqxToggleButton({toggled: false});
    $(".jqxButton12").on('click', function () {
        var toggled = $(".jqxButton12").jqxToggleButton('toggled');
    });
    $(".jqxButton13").jqxToggleButton({toggled: false});
    $(".jqxButton13").on('click', function () {
        var toggled = $(".jqxButton13").jqxToggleButton('toggled');
    });
    $(".jqxButton14").jqxToggleButton({toggled: false});
    $(".jqxButton14").on('click', function () {
        var toggled = $(".jqxButton14").jqxToggleButton('toggled');
    });
    $(".jqxButton15").jqxToggleButton({toggled: false});
    $(".jqxButton15").on('click', function () {
        var toggled = $(".jqxButton15").jqxToggleButton('toggled');
    });
    $(".jqxButton16").jqxToggleButton({toggled: false});
    $(".jqxButton16").on('click', function () {
        var toggled = $(".jqxButton16").jqxToggleButton('toggled');
    });
    $(".jqxButton18").jqxToggleButton({toggled: false});
    $(".jqxButton18").on('click', function () {
        var toggled = $(".jqxButton18").jqxToggleButton('toggled');
    });
    $(".jqxButtonNovoeNapravlenie").jqxToggleButton({toggled: false});
    $(".jqxButtonNovoeNapravlenie").on('click', function () {
        var toggled = $(".jqxButtonNovoeNapravlenie").jqxToggleButton('toggled');
    });
    $(".jqxButtonYdalitNapravlenie").jqxToggleButton({toggled: false});
    $(".jqxButtonYdalitNapravlenie").on('click', function () {
        var toggled = $(".jqxButtonYdalitNapravlenie").jqxToggleButton('toggled');
    });

});

//Таблица Grid
$(document).ready(function () {
    var url = "../sampledata/products.xml";
    // prepare the data
    var source =
        {
            datatype: "xml",
            datafields: [
                {name: 'ID', type: 'integer'},
                {name: 'ОМС', type: 'char'},
                {name: 'ФИО', type: 'char'},
                {name: 'Номер карты', type: 'char'},
                {name: 'Год', type: 'date'},
                {name: 'Учет с', type: 'date'},
                {name: 'ЖК, ведущая беременную', type: 'char'}
            ],
            root: "Products",
            record: "Product",
            id: 'ProductID',
            url: url
        };
    var cellsrenderer = function (row, columnfield, value, defaulthtml, columnproperties, rowdata) {
        if (value < 20) {
            return '<span style="margin: 4px; margin-top:8px; float: ' + columnproperties.cellsalign + '; color: #ff0000;">' + value + '</span>';
        } else {
            return '<span style="margin: 4px; margin-top:8px; float: ' + columnproperties.cellsalign + '; color: #008000;">' + value + '</span>';
        }
    }

    // initialize jqxGrid
    $("#grid").jqxGrid(
        {
            width: getWidth('Grid'),
            source: dataAdapter,
            pageable: true,
            autoheight: true,
            sortable: true,
            altrows: true,
            enabletooltips: true,
            editable: true,
            selectionmode: 'multiplecellsadvanced',
            columns: [
                {text: 'Product Name', columngroup: 'ProductDetails', datafield: 'ProductName', width: 250},
                {
                    text: 'Quantity per Unit',
                    columngroup: 'ProductDetails',
                    datafield: 'QuantityPerUnit',
                    cellsalign: 'right',
                    align: 'right',
                    width: 200
                },
                {
                    text: 'Unit Price',
                    columngroup: 'ProductDetails',
                    datafield: 'UnitPrice',
                    align: 'right',
                    cellsalign: 'right',
                    cellsformat: 'c2',
                    width: 200
                },
                {
                    text: 'Units In Stock',
                    datafield: 'UnitsInStock',
                    cellsalign: 'right',
                    cellsrenderer: cellsrenderer,
                    width: 100
                },
                {text: 'Discontinued', columntype: 'checkbox', datafield: 'Discontinued'}
            ],
            columngroups: [
                {text: 'Product Details', align: 'center', name: 'ProductDetails'}
            ]
        });
});

//Дата
$(document).ready(function () {
    $(".jqxDateTimeInput").jqxDateTimeInput({width: '125px', height: '25px'});
});

//inputы
$(document).ready(function () {
    $(".input1").jqxInput({height: 23, width: 40, minLength: 1});
    $(".input2").jqxInput({height: 23, width: 40, minLength: 1});
    $(".input3").jqxInput({height: 23, width: 40, minLength: 1});
    $(".input4").jqxInput({height: 23, width: 40, minLength: 1});
    $(".input5").jqxInput({height: 23, width: 40, minLength: 1});
    $(".input6").jqxInput({height: 23, width: 40, minLength: 1});
});

//комбобокс
$(document).ready(function () {
    var source = [
        "Нет",
        "Есть"
    ];
    // Create a jqxComboBox
    $(".jqxComboBox").jqxComboBox({selectedIndex: 1, source: source, width: '200px', height: '30px'});
});

//галочка(чекбокс)
$(document).ready(function () {
    $('.acceptInput').jqxCheckBox({width: 'auto'});
});

//номер телефона
$(document).ready(function () {
    // Create jqxMaskedInput
    $(".numericInput").jqxMaskedInput({width: '250px', height: '25px', mask: '#(###)###-##-##'});

});
$(document).ready(function () {
    $(".ds").on("input", function () {
        $(".in_ds").val(this.value);
    });
});

//радиобаттоны
$(document).ready(function () {
    $(".jqxRadioButton").jqxRadioButton({width: 250, height: 25});
});

//ползунок ds
$(document).ready(function () {
    const num = document.getElementById('numds');
    const rng = document.getElementById('rangeds');
    const view = document.getElementById('viewds');
    const goods = document.querySelectorAll('.good');
    const set = val => {
        num.value = val;
        rng.value = val;
        view.textContent = val;
        [...goods].forEach(good => {
            const options = good.querySelectorAll('.option');
            [...options].forEach(option => {
                option.style.display = val >= +option.dataset.from ? 'block' : 'none';
            });
        });
    }
    rng.addEventListener('input', () => set(rng.value));
    num.addEventListener('change', () => set(num.value));
});
//ползунок dc
$(document).ready(function () {
    const num = document.getElementById('numdc');
    const rng = document.getElementById('rangedc');
    const view = document.getElementById('viewdc');
    const goods = document.querySelectorAll('.good');
    const set = val => {
        num.value = val;
        rng.value = val;
        view.textContent = val;
        [...goods].forEach(good => {
            const options = good.querySelectorAll('.option');
            [...options].forEach(option => {
                option.style.display = val >= +option.dataset.from ? 'block' : 'none';
            });
        });
    }
    rng.addEventListener('input', () => set(rng.value));
    num.addEventListener('change', () => set(num.value));
});
//ползунок dt
$(document).ready(function () {
    const num = document.getElementById('numdt');
    const rng = document.getElementById('rangedt');
    const view = document.getElementById('viewdt');
    const goods = document.querySelectorAll('.good');
    const set = val => {
        num.value = val;
        rng.value = val;
        view.textContent = val;
        [...goods].forEach(good => {
            const options = good.querySelectorAll('.option');
            [...options].forEach(option => {
                option.style.display = val >= +option.dataset.from ? 'block' : 'none';
            });
        });
    }
    rng.addEventListener('input', () => set(rng.value));
    num.addEventListener('change', () => set(num.value));
});
//ползунок cd
$(document).ready(function () {
    const num = document.getElementById('numcd');
    const rng = document.getElementById('rangecd');
    const view = document.getElementById('viewcd');
    const goods = document.querySelectorAll('.good');
    const set = val => {
        num.value = val;
        rng.value = val;
        view.textContent = val;
        [...goods].forEach(good => {
            const options = good.querySelectorAll('.option');
            [...options].forEach(option => {
                option.style.display = val >= +option.dataset.from ? 'block' : 'none';
            });
        });
    }
    rng.addEventListener('input', () => set(rng.value));
    num.addEventListener('change', () => set(num.value));
});
//ползунок ce
$(document).ready(function () {
    const num = document.getElementById('numce');
    const rng = document.getElementById('rangece');
    const view = document.getElementById('viewce');
    const goods = document.querySelectorAll('.good');
    const set = val => {
        num.value = val;
        rng.value = val;
        view.textContent = val;
        [...goods].forEach(good => {
            const options = good.querySelectorAll('.option');
            [...options].forEach(option => {
                option.style.display = val >= +option.dataset.from ? 'block' : 'none';
            });
        });
    }
    rng.addEventListener('input', () => set(rng.value));
    num.addEventListener('change', () => set(num.value));
});
//ползунок cv
$(document).ready(function () {
    const num = document.getElementById('numcv');
    const rng = document.getElementById('rangecv');
    const view = document.getElementById('viewcv');
    const goods = document.querySelectorAll('.good');
    const set = val => {
        num.value = val;
        rng.value = val;
        view.textContent = val;
        [...goods].forEach(good => {
            const options = good.querySelectorAll('.option');
            [...options].forEach(option => {
                option.style.display = val >= +option.dataset.from ? 'block' : 'none';
            });
        });
    }
    rng.addEventListener('input', () => set(rng.value));
    num.addEventListener('change', () => set(num.value));
});


function render_okno_redaktirovanie_pazienta() {
    //Adding event listeners
    function _addEventListeners() {
        var toggled = null;
        $(".jqxButton7").jqxToggleButton({toggled: false});
        $(".jqxButton7").click(function () {
            toggled = $(".jqxButton7").jqxToggleButton('toggled');
            toggleCheck()
        });

        function toggleCheck() {
            if (toggled == true) {
                $('.window1').jqxWindow('open');
                $('.window1').jqxWindow('resizable', true);
            } else {
                $('.window1').jqxWindow('close');
                $('.window1').jqxWindow('draggable', true);
            }
        }
    };


    //Creating the demo window
    function _createWindow() {
        var jqxWidget = $('.jqxWidgetWindow1');
        var offset = jqxWidget.offset();
        $('.window1').jqxWindow({
            position: {x: offset.left + 50, y: offset.top + 50},
            showCollapseButton: true,
            maxHeight: 1000,
            maxWidth: 2200,
            minHeight: 400,
            minWidth: 700,
            height: 400,
            width: 700,
            autoOpen: false,
            initContent: function () {
                $('#tab').jqxTabs({height: '100%', width: '100%'});
                $('.window1').jqxWindow('focus');
            }
        });
    };
    return {
        config: {
            dragArea: null
        },
        init: function () {
            //Attaching event listeners
            _addEventListeners();
            _createWindow();
            $('.window1').jqxWindow('close');
        }
    };
}

$(function () {
    //Всплывающее окно Window
    render_okno_redaktirovanie_pazienta().init();
});
// fetch('url').then(function (response) {
//     response.json().then( function (data) {
//         const MEGA_DANIE_SPRAVOCHNIX_TABLIZ = data;
//             console.log(MEGA_DANIE_SPRAVOCHNIX_TABLIZ);
//             MEGA_DANIE_SPRAVOCHNIX_TABLIZ['mkb10'][0]
//    })
// });

//выбор доктора


$(document).ready(function () {
    var source = [];
    $(".jqxWidgetDropDoctor").jqxDropDownList({source: source, placeHolder: "Выбрать врача", width: 250, height: 30});
});

//ОКНО МБК10
function render_okno_mkb10() {
    //Adding event listeners
    function _addEventListeners() {
        var toggled = null;
        $(".jqxButton17").jqxToggleButton({toggled: false});
        $(".jqxButton17").click(function () {
            toggled = $(".jqxButton17").jqxToggleButton('toggled');
            toggleCheck()
        });

        function toggleCheck() {
            if (toggled == true) {
                $('.window2').jqxWindow('open');
                $('.window2').jqxWindow('resizable', true);
            } else {
                $('.window2').jqxWindow('close');
                $('.window2').jqxWindow('draggable', true);
            }
        }
    };


    //Creating the demo window
    function _createWindow() {
        var jqxWidget = $('.jqxWidgetWindow2');
        var offset = jqxWidget.offset();
        $('.window2').jqxWindow({
            position: {x: offset.left + 50, y: offset.top + 50},
            showCollapseButton: true,
            maxHeight: 1000,
            maxWidth: 2200,
            minHeight: 600,
            minWidth: 700,
            height: 400,
            width: 700,
            autoOpen: false,
            initContent: function () {
                $('#tab').jqxTabs({height: '100%', width: '100%'});
                $('.window2').jqxWindow('focus');

            }
        });
    };


    return {
        config: {
            dragArea: null
        },
        init: function () {
            //Attaching event listeners
            _addEventListeners();
            _createWindow();
        }
    };

}

$(function () {
    render_okno_mkb10().init();

});

//ОКНО Доктора
function render_okno_doctor() {
    //Adding event listeners
    function _addEventListeners() {
        var toggled = null;
        $(".jqxButton6").jqxToggleButton({toggled: false});
        $(".jqxButton6").click(function () {
            toggled = $(".jqxButton6").jqxToggleButton('toggled');
            toggleCheck()
        });

        function toggleCheck() {
            if (toggled == true) {
                $('.window3').jqxWindow('open');
                $('.window3').jqxWindow('resizable', true);
            } else {
                $('.window3').jqxWindow('close');
                $('.window3').jqxWindow('draggable', true);
            }
        }
    };


    //Creating the demo window
    function _createWindow() {
        var jqxWidget = $('.jqxWidgetWindow3');
        var offset = jqxWidget.offset();
        $('.window3').jqxWindow({
            position: {x: offset.left + 50, y: offset.top + 50},
            showCollapseButton: true,
            maxHeight: 1000,
            maxWidth: 2200,
            minHeight: 600,
            minWidth: 700,
            height: 400,
            width: 700,
            autoOpen: false,
            initContent: function () {
                $('#tab').jqxTabs({height: '100%', width: '100%'});
                $('.window3').jqxWindow('focus');

            }
        });
    };


    return {
        config: {
            dragArea: null
        },
        init: function () {
            //Attaching event listeners
            _addEventListeners();
            _createWindow();
        }
    };

}

$(function () {
    render_okno_doctor().init();

});

//ОКНО Консультации
function render_okno_konsultacii() {
    //Adding event listeners
    function _addEventListeners() {
        var toggled = null;
        $(".jqxButton3").jqxToggleButton({toggled: false});
        $(".jqxButton3").click(function () {
            toggled = $(".jqxButton3").jqxToggleButton('toggled');
            toggleCheck()
        });

        function toggleCheck() {
            if (toggled == true) {
                $('.window4').jqxWindow('open');
                $('.window4').jqxWindow('resizable', true);
            } else {
                $('.window4').jqxWindow('close');
                $('.window4').jqxWindow('draggable', true);
            }
        }
    };


    //Creating the demo window
    function _createWindow() {
        var jqxWidget = $('.jqxWidgetWindow4');
        var offset = jqxWidget.offset();
        $('.window4').jqxWindow({
            position: {x: offset.left + 50, y: offset.top + 50},
            showCollapseButton: true,
            maxHeight: 1000,
            maxWidth: 2200,
            minHeight: 600,
            minWidth: 700,
            height: 400,
            width: 700,
            autoOpen: false,
            initContent: function () {
                $('#tab').jqxTabs({height: '100%', width: '100%'});
                $('.window4').jqxWindow('focus');

            }
        });
    };


    return {
        config: {
            dragArea: null
        },
        init: function () {
            //Attaching event listeners
            _addEventListeners();
            _createWindow();
        }
    };

}

$(function () {
    render_okno_konsultacii().init();

});

//ОКНО Смены ЖК
function render_okno_smenaJK() {
    //Adding event listeners
    function _addEventListeners() {
        var toggled = null;
        $(".jqxButton4").jqxToggleButton({toggled: false});
        $(".jqxButton4").click(function () {
            toggled = $(".jqxButton4").jqxToggleButton('toggled');
            toggleCheck()
        });

        function toggleCheck() {
            if (toggled == true) {
                $('.window5').jqxWindow('open');
                $('.window5').jqxWindow('resizable', true);
            } else {
                $('.window5').jqxWindow('close');
                $('.window5').jqxWindow('draggable', true);
            }
        }
    };


    //Creating the demo window
    function _createWindow() {
        var jqxWidget = $('.jqxWidgetWindow5');
        var offset = jqxWidget.offset();
        $('.window5').jqxWindow({
            position: {x: offset.left + 50, y: offset.top + 50},
            showCollapseButton: true,
            maxHeight: 1000,
            maxWidth: 2200,
            minHeight: 600,
            minWidth: 700,
            height: 400,
            width: 700,
            autoOpen: false,
            initContent: function () {
                $('#tab').jqxTabs({height: '100%', width: '100%'});
                $('.window5').jqxWindow('focus');

            }
        });
    };


    return {
        config: {
            dragArea: null
        },
        init: function () {
            //Attaching event listeners
            _addEventListeners();
            _createWindow();
        }
    };

}

$(function () {
    render_okno_smenaJK().init();

});