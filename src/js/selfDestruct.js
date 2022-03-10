"use strict";
exports.__esModule = true;
exports.selfDestruct = void 0;
var artemis_1 = require("./artemis");
var selfDestruct = function () {
    artemis_1.output.innerHTML = '<p>Self-Destructing...</p>';
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
exports.selfDestruct = selfDestruct;
