var input = document.getElementById('input box');
var submit = document.getElementById('submit button');
// have the user type something in the box, and then when submit is clicked, trigger a function
input.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        submit.click();
    }
});


