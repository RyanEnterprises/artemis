"use strict";
exports.__esModule = true;
exports.versionNumber = exports.header = exports.output = exports.submit = exports.input = void 0;
var input = document.getElementById('input box');
exports.input = input;
var submit = document.getElementById('submit button');
exports.submit = submit;
var output = document.getElementById('response');
exports.output = output;
var header = document.getElementById('header');
exports.header = header;
var versionNumber = 4.0;
exports.versionNumber = versionNumber;
var arrays_1 = require("./arrays");
var selfDestruct_1 = require("./selfDestruct");
// when submit is clicked, take the text and run a function
submit.addEventListener('click', function () {
    // get the text from the input box
    var text = input.value;
    // clear the input box
    input.value = '';
    // run the function
    console.log(text);
    if (text.toLowerCase() === 'about') {
        output.innerHTML = '<p>Version: ' + versionNumber + '</p>';
    }
    else if (text.toLowerCase() === 'clear') {
        output.innerHTML = ' ';
    }
    else if (text.toLowerCase() === 'contact') {
        output.innerHTML = '<p>Email: <a href="mailto:rpmullin@comcast.net">link</a></p>';
    }
    else if (text.toLowerCase() === 'exit') {
        output.innerHTML = '<p>Exiting...</p>';
        setTimeout(function () {
            window.close();
        }, 4000);
    }
    else if (text.toLowerCase() === 'fact') {
        output.innerHTML = '<p>' + arrays_1.facts[Math.floor(Math.random() * arrays_1.facts.length)] + '</p>';
    }
    else if (text.toLowerCase() === 'github') {
        output.innerHTML = '<p>Github: <a href="https://github.com/RyanEnterprises/artemis">Link</a></p>';
    }
    else if (text.toLowerCase() === 'goodbye') {
        output.innerHTML = 'Goodbye!';
    }
    else if (text.toLowerCase() === 'hello') {
        output.innerHTML = 'Hello!';
    }
    else if (text.toLowerCase() === 'help') {
        output.innerHTML = 'Here are some helpful commands: <br> <br> <b>about</b> - displays information about the program <br> <b>clear</b> - clears the output box <br> <b>contact</b> - displays contact information <br> <b>exit</b> - closes the program <br> <b>fact</b> - gives a random fact <br> <b>github</b> - displays the github link <br> <b>help</b> - displays this message <br> <b>Joke</b> - tells you a joke <br> <b>license</b> - displays the license information <br> <b>Self-Destruct</b> - You\'ll see. <br> <b>version</b> - displays the version of the program <br>';
    }
    else if (text.toLowerCase() === 'hi') {
        output.innerHTML = "Hello";
    }
    else if (text.toLowerCase() === 'joke') {
        output.innerHTML = '<p>' + arrays_1.jokes[Math.floor(Math.random() * arrays_1.jokes.length)] + '</p>';
    }
    else if (text.toLowerCase() === 'license') {
        output.innerHTML = '<p> Licensed under the Apache License, Version 2.0 (the "License") <br> you may not use this file except in compliance with the License. <br> You may obtain a copy of the License at <a href="http://www.apache.org/licenses/LICENSE-2.0">Apache.org</a> <br> Unless required by applicable law or agreed to in writing, software <br> distributed under the License is distributed on an "AS IS" BASIS, <br> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. <br> See the License for the specific language governing permissions and <br> limitations under the License. </p>';
    }
    else if (text.toLowerCase() === 'self destruct') {
        (0, selfDestruct_1.selfDestruct)();
    }
    else {
        output.innerHTML = '<p>I don\'t understand that command. Try Again.</p>';
    }
});
