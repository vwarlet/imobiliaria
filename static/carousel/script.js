const carousel = document.getElementById("carousel"),
firstImg = carousel.querySelectorAll("img")[0],
arrowIcons = document.querySelectorAll(".wrapper i");

let isDragStart = false, isDragging = false, prevPageX, prevScrollLeft, positionDiff;

const showHideIcons = () => {
    // showing and hiding prev/next icon according to carousel scroll left value
    let scrollWidth = carousel.scrollWidth - carousel.clientWidth; // getting max scrollable width
    arrowIcons[0].style.display = carousel.scrollLeft == 0 ? "none" : "block";
    arrowIcons[1].style.display = carousel.scrollLeft == scrollWidth ? "none" : "block";
}

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        let firstImgWidth = firstImg.clientWidth + 14; // getting first img width & adding 14 margin value
        // if clicked icon is left, reduce width value from the carousel scroll left else add to it
        carousel.scrollLeft += icon.id == "left" ? -firstImgWidth : firstImgWidth;
        setTimeout(() => showHideIcons(), 60); // calling showHideIcons after 60ms
    });
});

const autoSlide = () => {
    // if there is no image left to scroll then return from here
    if(carousel.scrollLeft - (carousel.scrollWidth - carousel.clientWidth) > -1 || carousel.scrollLeft <= 0) return;

    positionDiff = Math.abs(positionDiff); // making positionDiff value to positive
    let firstImgWidth = firstImg.clientWidth + 14;
    // getting difference value that needs to add or reduce from carousel left to take middle img center
    let valDifference = firstImgWidth - positionDiff;

    if(carousel.scrollLeft > prevScrollLeft) { // if user is scrolling to the right
        return carousel.scrollLeft += positionDiff > firstImgWidth / 3 ? valDifference : -positionDiff;
    }
    // if user is scrolling to the left
    carousel.scrollLeft -= positionDiff > firstImgWidth / 3 ? valDifference : -positionDiff;
}

const dragStart = (e) => {
    // updatating global variables value on mouse down event
    isDragStart = true;
    prevPageX = e.pageX || e.touches[0].pageX;
    prevScrollLeft = carousel.scrollLeft;
}

const dragging = (e) => {
    // scrolling images/carousel to left according to mouse pointer
    if(!isDragStart) return;
    e.preventDefault();
    isDragging = true;
    carousel.classList.add("dragging");
    positionDiff = (e.pageX || e.touches[0].pageX) - prevPageX;
    carousel.scrollLeft = prevScrollLeft - positionDiff;
    showHideIcons();
}

const dragStop = () => {
    isDragStart = false;
    carousel.classList.remove("dragging");

    if(!isDragging) return;
    isDragging = false;
    autoSlide();
}

carousel.addEventListener("mousedown", dragStart);
carousel.addEventListener("touchstart", dragStart);

document.addEventListener("mousemove", dragging);
carousel.addEventListener("touchmove", dragging);

document.addEventListener("mouseup", dragStop);
carousel.addEventListener("touchend", dragStop);

document.querySelectorAll('#carousel img').forEach(item => {
    item.addEventListener('click', event => {
      document.getElementById('preview').src = event.target.src;
    });
  });

const prevPreviewButton = document.getElementById("prev-preview");
const nextPreviewButton = document.getElementById("next-preview");
const previewImage = document.getElementById('preview');
const carouselImages = document.querySelectorAll('#carousel img');
let currentImageIndex = 0;

// Função para mostrar a imagem de visualização atual
const showPreviewImage = (index) => {
  previewImage.src = carouselImages[index].src;

  // Verificar a posição atual e ocultar as setas apropriadas
  if (index === 0) {
    prevPreviewButton.style.display = "none"; // Esconder a seta esquerda na primeira imagem
    nextPreviewButton.style.display = "block"; // Mostrar a seta direita
  } else if (index === carouselImages.length - 1) {
    prevPreviewButton.style.display = "block"; // Mostrar a seta esquerda
    nextPreviewButton.style.display = "none"; // Esconder a seta direita na última imagem
  } else {
    prevPreviewButton.style.display = "block"; // Mostrar ambas as setas se não estiver na primeira nem na última imagem
    nextPreviewButton.style.display = "block";
  }
};

// Adicione um ouvinte de eventos às setas de navegação na visualização
prevPreviewButton.addEventListener("click", () => {
  if (currentImageIndex > 0) {
    currentImageIndex--;
    showPreviewImage(currentImageIndex);
  }
});

nextPreviewButton.addEventListener("click", () => {
  if (currentImageIndex < carouselImages.length - 1) {
    currentImageIndex++;
    showPreviewImage(currentImageIndex);
  }
});

// Chame showPreviewImage com o índice 0 para garantir que as setas estejam corretamente configuradas no início
showPreviewImage(0);

window.onload = function () {
    // Get the first image in the carousel
    var firstImage = document.getElementById('carousel').querySelector('img');
    // Get the preview image
    var previewImage = document.getElementById('preview');
    // Set the preview image source to the first carousel image source
    previewImage.src = firstImage.src;

    var previewImage = document.getElementById('preview');
    var imageNumber = document.getElementById('image-number');
  
    var images = document.querySelectorAll('#carousel img');
    var currentIndex = 0;
  
    function updatePreviewImage() {
      var currentImage = images[currentIndex];
      previewImage.src = currentImage.src;
      imageNumber.textContent = (currentIndex + 1) + '/' + images.length;
    }

    // Adicione um ouvinte de eventos para as miniaturas no carrossel para atualizar a imagem de visualização
    carouselImages.forEach((image, index) => {
      image.addEventListener('click', () => {
        currentIndex = index;
        updatePreviewImage();
      });
    });

    // Adicione event listeners para as setas esquerda e direita para controlar a navegação.
    // Atualize currentIndex e chame a função updatePreviewImage.
    document.getElementById('prev-preview').addEventListener('click', function () {
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      updatePreviewImage();
    });
  
    document.getElementById('next-preview').addEventListener('click', function () {
      currentIndex = (currentIndex + 1) % images.length;
      updatePreviewImage();
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowLeft') {
        // Tecla da seta para a esquerda
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updatePreviewImage();
      } else if (event.key === 'ArrowRight') {
        // Tecla da seta para a direita
        currentIndex = (currentIndex + 1) % images.length;
        updatePreviewImage();
      }
    });
  
    // Inicialize a visualização da imagem com a primeira imagem.
    updatePreviewImage();
  };
