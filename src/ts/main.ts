import { input, submit, output, header, versionNumber } from './artemis';
input.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        submit.click();
    }
});
