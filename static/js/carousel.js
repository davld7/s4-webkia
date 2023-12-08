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