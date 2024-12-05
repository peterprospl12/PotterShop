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
let slidesPerView = 2; // Domyślna liczba wyświetlanych slajdów (2)

function updateSlidesPerView() {
  const windowWidth = window.innerWidth;

  if (windowWidth <= 768) {
    slidesPerView = 1; // Na małych ekranach (smartfony) wyświetlamy 1 slajd
  } else if (windowWidth <= 979) {
    slidesPerView = 2; // Na średnich ekranach (tablety) wyświetlamy 2 slajdy
  } else if (windowWidth <= 1297) {
    slidesPerView = 3; // Na większych ekranach wyświetlamy 3 slajdy
  } else {
    slidesPerView = 4; // Na dużych ekranach wyświetlamy 4 slajdy
  }

  // Po aktualizacji liczby slajdów na ekranie, resetujemy pozycję slidera
  showSlide(currentSlide);
}

function showSlide(index) {
  const slides = document.querySelectorAll(".custom-slide");
  const totalSlides = slides.length;
  const iconPages = totalSlides - slidesPerView + 1;

  // Sprawdzamy, czy indeks nie przekracza granic
  if (index >= iconPages) {
    currentSlide = iconPages - 1;
  } else if (index < 0) {
    currentSlide = 0;
  } else {
    currentSlide = index;
    const slider = document.querySelector(".custom-slider");
    const slideWidth = slides[0].offsetWidth; // Szerokość jednego slajdu
    slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`; // Przesuwamy slider o odpowiednią szerokość
  }

  // Sprawdzamy, czy przyciski istnieją przed manipulowaniem nimi
  const arrowLeft = document.querySelector(".custom-prev");
  const arrowRight = document.querySelector(".custom-next");

  // Jeśli przyciski istnieją, wykonujemy dalsze operacje
  if (arrowLeft) {
    if (index == 0) {
      // Left arrow hide
      arrowLeft.classList.add("hide-custom-arrow");
    } else {
      arrowLeft.classList.remove("hide-custom-arrow");
    }
  }

  if (arrowRight) {
    if (index == iconPages - 1) {
      // Right arrow hide
      arrowRight.classList.add("hide-custom-arrow");
    } else {
      arrowRight.classList.remove("hide-custom-arrow");
    }
  }
}

function moveSlide(step) {
  showSlide(currentSlide + step); // Zmieniamy slajd o 1 w zależności od przycisku
}

// Inicjalne ustawienie slidera
updateSlidesPerView(); // Ustawiamy liczbę slajdów przy załadowaniu
showSlide(currentSlide);

// Nasłuchujemy zmian rozmiaru okna, aby dynamicznie dostosować liczbę wyświetlanych slajdów
window.addEventListener("resize", updateSlidesPerView);
