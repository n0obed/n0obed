// var header = document.getElementsByClassName("navbar-custom")
const nav = document.querySelector('.navbar-custom')
const getOffset = () => {
if(window.pageYOffset > 50){
    nav.style.backgroundColor = 'rgba(33, 37, 41, 0.5)';
    nav.style.transition = 'background 0.5s ease-out';
}
if (window.pageYOffset < 50) {
    nav.style.backgroundColor = 'rgba(33, 37, 41, 1)';
}
}

window.addEventListener('scroll', getOffset)