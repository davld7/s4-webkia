document.addEventListener("DOMContentLoaded", function () {
    const indexLink = document.getElementById("index");
    const aboutLink = document.getElementById("about");
    const companyLink = document.getElementById("company");
    const vehiclesLink = document.getElementById("vehicles");
    const contactLink = document.getElementById("contact");
    const adminLink = document.getElementById("admin");

    indexLink.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "/";
    });

    aboutLink.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "/about/";
    });

    companyLink.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "/company/";
    });

    vehiclesLink.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "/vehicles/";
    });

    contactLink.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "/contact/";
    });

    adminLink.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "/admin/";
    });
});

const images = document.querySelectorAll("#imageCarousel img");
let currentIndex = 0;

function showImage(index) {
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }
    images[index].style.display = "block";
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
}

function previousImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
}

document.getElementById("previousButton").addEventListener("click", previousImage);
document.getElementById("nextButton").addEventListener("click", nextImage);

showImage(currentIndex);