const accoutnsBtn = document.getElementById('social-media-btn');
const accoutnsDiv = document.getElementById('social-media');
const rightArrow = document.getElementById('fa-right') ;
const downArrow = document.getElementById('fa-down');
let isOn = false;

accoutnsBtn.addEventListener('click', () => {
    if (!isOn){
        accoutnsDiv.style.display = 'block';
        rightArrow.style.display = 'none';
        downArrow.style.display = 'block';
        isOn = true;
        window.scrollTo(0, 1000)
    } else {
        accoutnsDiv.style.display = 'none';
        rightArrow.style.display = 'block';
        downArrow.style.display = 'none';
        isOn = false;
    }
});