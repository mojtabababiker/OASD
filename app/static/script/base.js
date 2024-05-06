const collapseNavBtn = document.getElementById('collapse-nav-btn');
const navBar = document.getElementById('nav-bar');
const openCollapse = document.getElementById('open-nav');
const closeCollaps = document.getElementById('close-nav');
const collapseSchBtn = document.getElementById('collapse-search-btn');

const searchBar = document.getElementById('search-bar');
const searchDiv = document.getElementById('search-form');
const showDivBtn = document.getElementById('search-btn');
const showDivIcon = document.getElementById('search-icon');
const formDiv = document.getElementById('form-group');
const closeDiv = document.getElementById('close-search');

let collapsedNav = true;
let collapsedSch = true;
collapseNavBtn.addEventListener('click', () => {
    if (collapsedNav) {
        openCollapse.style.opacity = '0'
        closeCollaps.style.opacity = '1';
        navBar.style.left = '0px';
        collapsedNav = false;
    } else {
        closeCollaps.style.opacity = '0';
        openCollapse.style.opacity = '1'
        navBar.style.left = '-2000px';
        collapsedNav = true;
    }
})

collapseSchBtn.addEventListener('click', () => {
    if (collapsedSch) {
        searchBar.style.top = '60px';
        searchBar.style.left = 'auto';
        collapsedSch = false;
    } else {
        searchBar.style.top = '-1000px';
        collapsedSch = true
    }
})

showDivBtn.addEventListener('click', () => {

    if (searchDiv.classList.contains('dnone')){
        searchDiv.classList.remove('dnone');
        setTimeout(()=>{
            formDiv.style.left = 'auto';
            closeDiv.style.top = '10%'
        }, 600)
    } else {
        searchDiv.classList.add('dnone')
    }
})
closeDiv.addEventListener('click', ()=> {
    closeDiv.style.top = '-100%';
    formDiv.style.left = '-200%';
    setTimeout(()=> {
        searchDiv.classList.add('dnone');
    }, 600)
})

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeDiv.style.top = '-100%';
        formDiv.style.left = '-200%';
        setTimeout(()=> {
            searchDiv.classList.add('dnone');
        }, 600)
    }
})