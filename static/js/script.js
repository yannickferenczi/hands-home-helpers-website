/* Open Toolbox */

let toolbox = document.getElementsByClassName("user-options-trigger");

console.log(toolbox);
if (toolbox.length !== 0) {
    toolbox[0].addEventListener("click", function () {
        let tools = document.getElementsByClassName("user-options");
        tools[0].classList.toggle("show");
    });
}

/* Review showslide */

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides((slideIndex += n));
}

function currentSlide(n) {
    showSlides((slideIndex = n));
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    if (slides.length >= 1) {
        if (n > slides.length) {
            slideIndex = 1;
        }
        if (n < 1) {
            slideIndex = slides.length;
        }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex - 1].style.display = "block";
}
}


/* Messages disapearance */

setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
