const sliderLeft = document.querySelector('.fa-chevron-left');
const sliderRight = document.querySelector('.fa-chevron-right');
const sliderLine = document.querySelector('.failed-tasks-slider-line');
const sliderLineItems = document.querySelectorAll('.failed-tasks-slider-line div');
let sliderOffset = 0;
let maxOffset = (sliderLineItems.length - 6) * 330;

sliderRight.addEventListener('click', () => {
    sliderOffset = sliderOffset - 330;
    if (sliderOffset < -maxOffset) {
        sliderOffset = -maxOffset;
    }
    sliderLine.style.left = sliderOffset + 'px';
});

sliderLeft.addEventListener('click', () => {
    sliderOffset = sliderOffset + 330;
    if (sliderOffset > 0) {
        sliderOffset = 0;
    }
    sliderLine.style.left = sliderOffset + 'px';
})