const profileImg = document.getElementById('profile-img-btn');
const imgDialog = document.getElementById('profile_img');
const passwd1 = document.getElementById('passwd-1');
const passwd2 = document.getElementById('passwd-2');
const password = document.getElementById('password');
const arrowDown = document.getElementById('pw-arrow-down');
const arrowRight = document.getElementById('pw-arrow-right');
const toggle = document.getElementById('chpwd-btn');
let On = false;

const passwd = password.getAttribute('value')
passwd1.firstElementChild.setAttribute('type', "password")
passwd2.firstElementChild.setAttribute('type', "password")
console.log(passwd)

toggle.addEventListener('click', () => {
    if (!On){
        arrowDown.style.display = 'block';
        arrowRight.style.display = 'none';
        passwd1.firstElementChild.setAttribute('value', "")
        passwd2.firstElementChild.setAttribute('value', "")
        passwd1.style.display = 'block';
        passwd2.style.display = 'block';
        On = true;
    } else {
        arrowDown.style.display = 'none';
        arrowRight.style.display = 'block';
        passwd1.style.display = 'none';
        passwd2.style.display = 'none';
        passwd1.firstElementChild.setAttribute('value', passwd)
        passwd2.firstElementChild.setAttribute('value', passwd)
        On = false;
    }
})

profileImg.addEventListener('click', () => {
    imgDialog.click()
})

imgDialog.addEventListener('change', () => {
    const file = imgDialog.files[0];
    const fr = new FileReader();
    fr.onload = (event) => {
        profileImg.style.backgroundImage = 'none'
        profileImg.style.backgroundImage = event.target.result
        console.log(event.target.result)
    };
    fr.readAsDataURL(file)
})