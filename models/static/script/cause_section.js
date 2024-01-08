const swiperLeft = document.getElementById('swip-left');
const swiperRight = document.getElementById('swip-right');
console.log(swiperLeft)
console.log(swiperRight)
$(document).ready(function(){
    $('.cause-slider').slick({
        infinite: true,
        autoplay: true,
        lazyLoad: true,
        prevArrow: swiperLeft,
        nextArrow: swiperRight,
        autoplaySpeed: 30000,
        // speed: 500,
        // fade: true,
        // centerMode: true,
        pauseOnFocus: true,
        pauseOnHover: true,
        waitForAnimate: false,
        cssEase: 'ease-in-out'
    });
  });