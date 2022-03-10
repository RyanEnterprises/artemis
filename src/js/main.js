"use strict";
exports.__esModule = true;
var artemis_1 = require("./artemis");
artemis_1.input.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        artemis_1.submit.click();
    }
});
