const table = {
    "zh-tw": {
        selectLang: "繁體中文",
        login: "登入",
        hello: "您好,歡迎",
    },
    "en": {
        selectLang: "English",
        login: "Login",
        hello: "Hello,Welcome",
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
    get selectLang() {
        return this.data.selectLang
    }
    /**
     * used for login button
     */
    get login() {
        return this.data.login
    }
    /**
     * pop up greeting message
     */
    get hello() {
        return this.data.hello
    }
}
