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
    if (text.toLowerCase() === 'help') {
        output.innerHTML = 'Here are some helpful commands: <br> <br> <b>about</b> - displays information about the program <br> <b>clear</b> - clears the output box <br> <b>contact</b> - displays contact information <br> <b>exit</b> - closes the program <br> <b>github</b> - displays the github link <br> <b>help</b> - displays this message <br> <b>license</b> - displays the license information <br> <b>version</b> - displays the version of the program <br>'; 
    } 
    else if (text.toLowerCase() === 'clear') {
        output.innerHTML = ' ';
    }
    else if (text.toLowerCase() === 'hello') {
        output.innerHTML = 'Hello!';
    }
    else if (text.toLowerCase() === 'hi') {
        alert("Hello");
    }
    else if (text.toLowerCase() === 'goodbye') {
        alert("GOODBYE");
    }
    

});