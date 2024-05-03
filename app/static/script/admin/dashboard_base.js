const sections = document.querySelectorAll('.res-nv');

const sideBarToggler = document.getElementById('sidebar-toggle');
const sideBar = document.getElementById('sideBar');
const openSearch = document.getElementById('search');
const searchBar = document.getElementById('searchBar');
const closeSearch = document.getElementById('close-search-btn');
const searchBtn = document.getElementById('search-btn');
// const serachInput = document.querySelector('.search-form');
const serachInput = document.getElementById('search-input');

let sideBarOn = true;

function logSearch(KeyboardEvent) {
    if (KeyboardEvent.key === "Enter") {
        alert(serachInput.value)
    }
};

openSearch.addEventListener('click', () => {
    openSearch.classList.add('hide');
    searchBar.classList.remove('hide');
    
    window.addEventListener('keydown', logSearch)
});
closeSearch.addEventListener('click', () =>{
    searchBar.classList.add('hide');
    openSearch.classList.remove('hide');
    window.removeEventListener('keydown', logSearch)
});

searchBtn.addEventListener('click', () => {
    alert(serachInput.value)
});

sideBarToggler.addEventListener('click', () => {
    if (sideBarOn) {
        sideBar.classList.add('hide-side');
        sections.forEach(section => {
            section.classList.remove('section');
        });
        sideBarOn = false;
    } else {
        sideBar.classList.remove('hide-side');
        sections.forEach(section => {
            section.classList.add('section');
        });
        sideBarOn = true;
    }
})
