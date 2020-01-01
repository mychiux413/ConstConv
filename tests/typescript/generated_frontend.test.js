"use strict";
exports.__esModule = true;
var generated_frontend_1 = require("./generated_frontend");
var compare = function (expect_value, actual_value) {
    if (expect_value !== actual_value) {
        return "[Error] expect '" + expect_value + "' but got '" + actual_value + "'\n";
    }
    return "";
};
var errs = "";
errs += compare(generated_frontend_1.ml.Hello, "您好,歡迎");
errs += compare(generated_frontend_1.ml.Login, "登入");
errs += compare(generated_frontend_1.ml.SelectLang, "繁體中文");
generated_frontend_1.setLang("en");
errs += compare(generated_frontend_1.ml.Hello, "Hello,Welcome");
errs += compare(generated_frontend_1.ml.Login, "Login");
errs += compare(generated_frontend_1.ml.SelectLang, "English");
if (errs !== "") {
    throw errs;
}
