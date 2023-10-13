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