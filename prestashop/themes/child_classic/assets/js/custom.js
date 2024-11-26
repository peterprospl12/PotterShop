const menu = document.getElementById("_desktop_top_menu");
const sticky = menu.offsetTop;

window.addEventListener(
  "scroll",
  function () {
    if (this.window.scrollY > sticky) {
      menu.classList.add("sticky");
    } else {
      menu.classList.remove("sticky");
    }
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
