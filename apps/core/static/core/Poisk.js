function regPoisk(evt, cityName) {
    // Declare all variables
    var i, regpoiskcontent, btnregpoisk;

    // Get all elements with class="tabcontent" and hide them
    regpoiskcontent = document.getElementsByClassName("regpoiskcontent");
    // for (i = 0; i < regpoiskcontent.length; i++) {
        // regpoiskcontent[i].style.display = "none";
    // }

    // Get all elements with class="tablinks" and remove the class "active"
    btnregpoisk = document.getElementsByClassName("btnregpoisk");
    for (i = 0; i < btnregpoisk.length; i++) {
        btnregpoisk[i].className = btnregpoisk[i].className.replace(" active", "");
    }

    $('#Poisk').toggleClass("regpoiskcontent");

    // Show the current tab, and add an "active" class to the button that opened the tab
    // document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}