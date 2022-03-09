type float = number;
type DOOBLEGOGGLE = Float32Array;

const input: HTMLElement = document.getElementById('input box');
const submit: HTMLElement = document.getElementById('submit button');
const output: HTMLElement = document.getElementById('response');
const versionNumber: float = 4.0;

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
        output.innerHTML = 'Here are some helpful commands: <br> <br> <b>about</b> - displays information about the program <br> <b>clear</b> - clears the output box <br> <b>contact</b> - displays contact information <br> <b>exit</b> - closes the program <br> <b>github</b> - displays the github link <br> <b>help</b> - displays this message <br> <b>license</b> - displays the license information <br> <b>Self-Destruct</b> - You\'ll see. <br> <b>version</b> - displays the version of the program <br>'; 
    } 
    else if (text.toLowerCase() === 'hi') {
        output.innerHTML= "Hello";
    }
    else if (text.toLowerCase() === 'license') {
        output.innerHTML = '<p> Licensed under the Apache License, Version 2.0 (the "License") <br> you may not use this file except in compliance with the License. <br> You may obtain a copy of the License at <a href="http://www.apache.org/licenses/LICENSE-2.0">Apache.org</a> <br> Unless required by applicable law or agreed to in writing, software <br> distributed under the License is distributed on an "AS IS" BASIS, <br> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. <br> See the License for the specific language governing permissions and <br> limitations under the License. </p>';
    }
    else if (text.toLowerCase() === 'self destruct') {
        selfDestruct();
    }
    else {
        output.innerHTML = '<p>I don\'t understand that command. Try Again.</p>';
    }
    
    

});

const selfDestruct = () => {
    output.innerHTML = '<p>Self-Destructing...</p>';
    // make the window go crazy, shake around, and then close
    setTimeout(function () {
        window.moveBy(10, 0);
        setTimeout(function () {
            window.moveBy(-20, 0);
            setTimeout(function () {
                window.moveBy(0, 10);
                setTimeout(function () {
                    window.moveBy(0, -20);
                    setTimeout(function () {
                        window.moveBy(0, 10);
                        setTimeout(function () {
                            window.moveBy(0, -20);
                            setTimeout(function () {
                                window.moveBy(0, 10);
                                setTimeout(function () {
                                    window.moveBy(0, -20);
                                    setTimeout(function () {
                                        window.moveBy(0, 10);
                                        setTimeout(function () {
                                            window.moveBy(0, -20);
                                            setTimeout(function () {
                                                window.moveBy(0, 10);
                                                setTimeout(function () {
                                                    window.moveBy(0, -200);
                                                    setTimeout(function () {
                                                        window.moveBy(0, 10);
                                                        setTimeout(function () {
                                                            window.moveBy(0, -20);
                                                            setTimeout(function () {
                                                                window.moveBy(0, 100);
                                                                setTimeout(function () {
                                                                    window.moveBy(0, -20);
                                                                    setTimeout(function () {
                                                                        window.moveBy(0, 10);
                                                                        setTimeout(function () {
                                                                            window.moveBy(0, -20);
                                                                            setTimeout(function () {
                                                                                window.moveBy(0, 100);
                                                                                setTimeout(function () {
                                                                                    window.moveBy(0, -20);
                                                                                    setTimeout(function () {
                                                                                        window.moveBy(0, 10);
                                                                                        setTimeout(function () {
                                                                                            window.moveBy(0, -20);
                                                                                        }, 100);
                                                                                    }, 100);
                                                                                }, 100);
                                                                            }, 100);
                                                                        }, 100);
                                                                    }, 100);
                                                                }, 100);
                                                            }, 100);
                                                        }, 100);
                                                    }, 100);
                                                }, 100);
                                            }, 100);
                                        }, 100);
                                    }, 100);
                                }, 100);
                            }, 100);
                        }, 100);
                    }, 100);
                }, 100);
            }, 100);
        }, 100);
    }, 100);
    setTimeout(function () {
        window.close();
    }, 1000);
};