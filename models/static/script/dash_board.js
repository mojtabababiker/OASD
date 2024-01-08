const menuTogglers = document.getElementsByClassName("menu-toggle");


for (let i = 0; i < menuTogglers.length; i++) {
    let menuToggler = menuTogglers[i];
    const rightArrow = menuToggler.nextElementSibling;
    const downArrow = rightArrow.nextElementSibling;
    menuToggler.addEventListener('click', () => {

        if (menuToggler.parentElement.nextElementSibling.classList.contains('menu')){
            menuToggler.parentElement.nextElementSibling.classList.remove('menu')
            menuToggler.parentElement.style.borderBottom = 'none'
            menuToggler.parentElement.nextElementSibling.style.borderBottom = '#afadad 1px solid'
            rightArrow.style.display = 'none'
            downArrow.style.display = 'inline'
    
        } else {
            menuToggler.parentElement.nextElementSibling.classList.add('menu')
            menuToggler.parentElement.style.borderBottom = '#afadad 1px solid'
            downArrow.style.display = 'none'
            rightArrow.style.display = 'inline'
        }
    });
    
}; 