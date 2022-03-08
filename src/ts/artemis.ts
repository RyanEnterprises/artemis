const input = document.getElementById('input box');
const submit = document.getElementById('submit button');
const output = document.getElementById('response');

// when submit is clicked, take the text and run a function
submit.addEventListener('click', function () {
    // get the text from the input box
    var text = input.value;
    // clear the input box
    input.value = '';
    // run the function
    console.log(text);
    if (text.toLowerCase() === 'hello') {
        output.innerHTML = 'Hello!';
    }
    else if (text.toLowerCase() === 'hi') {
        alert("Hello");
    }
    else if (text.toLowerCase() === 'goodbye') {
        alert("GOODBYE");
    }
    else if (text.toLowerCase() === 'help') {
        
    }

});