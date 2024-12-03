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
