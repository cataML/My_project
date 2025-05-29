// static/js/main.js

document.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.querySelector('.menu-toggle');
  const navbarLinks = document.querySelector('.navbar-links');

  if (toggleButton && navbarLinks) {
    toggleButton.addEventListener('click', () => {
      navbarLinks.classList.toggle('active');
    });
  }
});
