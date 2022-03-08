var input = document.getElementById('input box');
var submit = document.getElementById('submit button');
// when submit is clicked, take the text and run a function
submit.addEventListener('click', function () {
    // get the text from the input box
    var text = input.value;
    // clear the input box
    input.value = '';
    // run the function
    console.log(text);
    if (text.toLowerCase() === 'hello') {
        alert(Math.floor(Math.floor(Math.random() * (hellos.length - 0.01))));
    }
});
// Arrays
var hellos = [
    'Hello',
    'Bonjour',
    'Hola',
    'Hallo',
    'Ciao',
    'Salut',
    'Guten Tag',
    'Namaste',
];
