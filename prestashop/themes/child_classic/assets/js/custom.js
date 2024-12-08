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

const imageContainer = document.querySelector('.product-cover');
const image = document.querySelector('.product-cover img');

imageContainer.addEventListener('mousemove', (e) => {
  // Pobieramy pozycję kursora w obrębie kontenera
  const { left, top, width, height } = imageContainer.getBoundingClientRect();
  const x = e.clientX - left; // Pozycja kursora w poziomie
  const y = e.clientY - top; // Pozycja kursora w pionie

  // Obliczamy procentowe położenie kursora
  const xPercent = (x / width) * 100;
  const yPercent = (y / height) * 100;

  // Ustawiamy tło, które będzie powiększonym fragmentem obrazu
  image.style.transform = `scale(3)`; // Powiększamy obraz 2 razy
  image.style.transformOrigin = `${xPercent}% ${yPercent}%`; // Przesuwamy tło w kierunku kursora
});

imageContainer.addEventListener('mouseleave', () => {
  // Resetowanie transformacji, gdy kursor opuści obrazek
  image.style.transform = `scale(1)`; // Przywracamy oryginalny rozmiar
});

// Open the modal with the selected image
function openModal(imageSrc) {
  var modal = document.getElementById('imageModal');
  var modalImage = document.getElementById('modalImage');
  
  // Set the modal image to the clicked image's source
  modal.style.display = "block";
  modalImage.src = imageSrc;
}

// Close the modal
function closeModal() {
  var modal = document.getElementById('imageModal');
  modal.style.display = "none";
}

///////////////////////////////////////////////////////////////////////////////

let currentSlide2 = 0;

function showSlide2(index) {
  const slides = document.querySelectorAll(".custom-slide2");
  const totalSlides = slides.length;
  const iconPages = totalSlides;

  // Sprawdzamy, czy indeks nie przekracza granic
  if (index >= iconPages) {
    currentSlide2 = iconPages - 1;
  } else if (index < 0) {
    currentSlide2 = 0;
  } else {
    currentSlide2 = index;
    const slider = document.querySelector(".custom-slider2");
    const slideWidth = slides[0].offsetWidth; // Szerokość jednego slajdu
    slider.style.transform = `translateX(-${currentSlide2 * slideWidth}px)`; // Przesuwamy slider o odpowiednią szerokość
  }

  // Sprawdzamy, czy przyciski istnieją przed manipulowaniem nimi
  const arrowLeft = document.querySelector(".custom-prev2");
  const arrowRight = document.querySelector(".custom-next2");

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

function moveSlide2(step) {
  showSlide2(currentSlide2 + step); // Zmieniamy slajd o 1 w zależności od przycisku
}

showSlide2(currentSlide2);