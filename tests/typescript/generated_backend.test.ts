import { MultiLangs } from "./generated_backend"

const compare = (expect_value: string, actual_value: string): string => {
    if (expect_value !== actual_value) {
        return `[Error] expect '${expect_value}' but got '${actual_value}'\n`
    }
    return ""
}

const ml = new MultiLangs("zh-tw")
let errs = ""
errs += compare(ml.hello, "您好,歡迎")
errs += compare(ml.login, "登入")
errs += compare(ml.selectLang, "繁體中文")
ml.setLang("en")
errs += compare(ml.hello, "Hello,Welcome")
errs += compare(ml.login, "Login")
errs += compare(ml.selectLang, "English")

if (errs !== "") {
    throw errs
}
