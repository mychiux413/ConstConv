import { ml, setLang } from "./generated_frontend.mjs"

var compare = function(expect_value, actual_value) {
    if (expect_value !== actual_value) {
        return `[Error] expect '${expect_value}' but got '${actual_value}'\n`
    }
    return ""
}

var errs = ""
errs += compare(ml.hello, "您好,歡迎")
errs += compare(ml.login, "登入")
errs += compare(ml.selectLang, "繁體中文")
setLang("en")
errs += compare(ml.hello, "Hello,Welcome")
errs += compare(ml.login, "Login")
errs += compare(ml.selectLang, "English")

if (errs !== "") {
    throw errs
}
