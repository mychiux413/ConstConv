const table = {
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
}

export class MultiLangs {
    constructor(langCode) {
        this.setLang(langCode)
    }
    setLang(langCode) {
        if (!(langCode in table)) {
            console.error(`language code ${langCode} doesn't exists in Language Table.`)
            return
        }
        this.data = table[langCode]
    }
    /**
     * # select language
     */
    get SelectLang() {
        return this.data.SelectLang
    }
    /**
     * used for login button
     */
    get Login() {
        return this.data.Login
    }
    /**
     * pop up greeting message
     */
    get Hello() {
        return this.data.Hello
    }
}
