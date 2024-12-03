const menu = document.getElementById("_desktop_top_menu");
const sticky = menu.offsetTop;
var lastScrollTop = 0;

window.addEventListener(
  "scroll",
  function () {
    if (this.window.scrollY > sticky) {
      menu.classList.add("sticky");
    } else {
      menu.classList.remove("sticky");
    }

    /*
    var st = window.scrollY || document.documentElement.scrollTop;

    if (st > lastScrollTop) {
      menu.style.top = "-60px";
    } else {
      menu.style.top = "0";
    }
    lastScrollTop = st <= 0 ? 0 : st;
    */
  },
  false
);

const toTop = document.querySelector(".to-top");

window.addEventListener("scroll", function () {
  if (this.window.scrollY > 300) {
    toTop.classList.add("active");
  } else {
    toTop.classList.remove("active");
  }
});

let currentSlide = 0;

function showSlide(index) {
  const slides = document.querySelectorAll(".slide");
  const totalSlides = slides.length;

  if (index >= totalSlides) {
    currentSlide = 0; // Wracamy do pierwszego zdjęcia
  } else if (index < 0) {
    currentSlide = totalSlides - 1; // Przechodzimy na ostatnie zdjęcie
  } else {
    currentSlide = index;
  }

  const slider = document.querySelector(".slider");
  slider.style.transform = `translateX(-${currentSlide * 100}%)`; // Przesuwamy slider
}

function moveSlide(step) {
  showSlide(currentSlide + step); // Zmieniamy slajd o 1 w zależności od przycisku
}

// Inicjalne ustawienie slidera
showSlide(currentSlide);
