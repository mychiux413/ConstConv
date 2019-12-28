"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var table = {
    "zh-tw": {
        SelectLang: "繁體中文",
        Login: "登入",
        Hello: "您好,歡迎",
    },
    "en": {
        SelectLang: "English",
        Login: "Login",
        Hello: "Hello,Welcome",
    },
};
var target = table["zh-tw"];
var MultiLangs = /** @class */ (function () {
    function MultiLangs() {
    }
    Object.defineProperty(MultiLangs.prototype, "SelectLang", {
        /**
         * # select language
         */
        get: function () {
            return target.SelectLang;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(MultiLangs.prototype, "Login", {
        /**
         * used for login button
         */
        get: function () {
            return target.Login;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(MultiLangs.prototype, "Hello", {
        /**
         * pop up greeting message
         */
        get: function () {
            return target.Hello;
        },
        enumerable: true,
        configurable: true
    });
    return MultiLangs;
}());
/**
 * @param langCode  set to change instance `ml`'s language
 */
exports.setLang = function (langCode) {
    if (!(langCode in table)) {
        console.error("language code " + langCode + " doesn't exists in Language Table.");
        return;
    }
    target = table[langCode];
};
/**
 * use instance `ml` to get language content which you've set from csv file before
 * use `setLang(<LanguageCode>)` to change the language you want
 */
exports.ml = new MultiLangs();
