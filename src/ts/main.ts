var input = document.getElementById('input box');
var submit = document.getElementById('submit button');
// have the user type something in the box, and then when submit is clicked, trigger a function
input.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        submit.click();
    }
});

// when submit is clicked, take the text and run a function
submit.addEventListener('click', function () {
    // get the text from the input box
    var text = input.value;
    // clear the input box
    input.value = '';
    // run the function
    console.log(text);
    if (text === 'z') {
        alert('Hello World');
    }
});