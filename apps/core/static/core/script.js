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
    $(".jqxButton3").jqxToggleButton({toggled: false});
    $(".jqxButton3").on('click', function () {
        var toggled = $(".jqxButton3").jqxToggleButton('toggled');
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
        var toggled = $(".jqxButton16").jqxToggleButton('toggled');
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
        $('.resizeCheckBox').on('change', function (event) {
            if (event.args.checked) {
                $('.window1').jqxWindow('resizable', true);
            } else {
                $('.window1').jqxWindow('resizable', false);
            }
        });
        $('.dragCheckBox').on('change', function (event) {
            if (event.args.checked) {
                $('.window1').jqxWindow('draggable', true);
            } else {
                $('.window1').jqxWindow('draggable', false);
            }
        });
        $('.showWindowButton1').click(function () {
            $('.window1').jqxWindow('open');
        });
        $('.hideWindowButton1').click(function () {
            $('.window1').jqxWindow('close');
        });
    };

    //Creating all page elements which are jqxWidgets
    function _createElements() {
        $('.showWindowButton1').jqxButton({width: '70px'});
        $('.hideWindowButton1').jqxButton({width: '65px'});
        $('.resizeCheckBox1').jqxCheckBox({width: '185px', checked: true});
        $('.dragCheckBox1').jqxCheckBox({width: '185px', checked: true});
    };

    //Creating the demo window
    function _createWindow() {
        var jqxWidget = $('.jqxWidgetWindow');
        var offset = jqxWidget.offset();
        $('.window1').jqxWindow({
            position: {x: offset.left + 50, y: offset.top + 50},
            showCollapseButton: true,
            maxHeight: 1000,
            maxWidth: 1200,
            minHeight: 400,
            minWidth: 700,
            height: 400,
            width: 700,
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
            //Creating all jqxWindgets except the window
            _createElements();
            //Attaching event listeners
            _addEventListeners();
            //Adding jqxWindow
            _createWindow();
        }
    };

}

$(function () {
    // fetch('url').then(function (response) {
    //     response.json().then( function (data) {
    //         const MEGA_DANIE_SPRAVOCHNIX_TABLIZ = data;
    //             console.log(MEGA_DANIE_SPRAVOCHNIX_TABLIZ);
    //             MEGA_DANIE_SPRAVOCHNIX_TABLIZ['mkb10'][0]
    //    })
    // });

    //Всплывающее окно Window
    render_okno_redaktirovanie_pazienta().init();
});


//выбор доктора


$(document).ready(function () {
    var source = [];
    $(".jqxWidgetDropDoctor").jqxDropDownList({source: source, placeHolder: "Выбрать врача", width: 250, height: 30});
});


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
        var jqxWidget = $('.jqxWidgetWindow');
        var offset = jqxWidget.offset();
        $('.window2').jqxWindow({
            position: {x: offset.left + 50, y: offset.top + 50},
            showCollapseButton: true,
            maxHeight: 1000,
            maxWidth: 2200,
            minHeight: 400,
            minWidth: 700,
            height: 400,
            width: 700,
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
            //Adding jqxWindow
            _createWindow();
        }
    };

}

$(function () {
    render_okno_mkb10().init();
});