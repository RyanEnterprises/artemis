const input = document.getElementById('input box');
const submit = document.getElementById('submit button');
const logo = document.querySelector('logo');
// have the user type something in the box, and then when submit is clicked, trigger a function
input.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        submit.click();
    }
});
let logoCounter = 0;
logo.addEventListener('click', function () {
    logoCounter++;
    if (logoCounter === 10) {
        logo.innerHTML = '<img src="https://th.bing.com/th/id/OIP.EGNIXLyZpW6t2rxPdv8ogQHaJ4?pid=ImgDet&rs=1" alt="the REAL Artemis" />';
    }
});
