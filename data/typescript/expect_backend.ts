interface LangData {
    selectLang: string
    login: string
    hello: string
}

type LangCode = "zh-tw" | "en"

type LangTable = {
    [code in LangCode]: LangData
}

const table: LangTable = {
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
    private data: LangData
    constructor(langCode: LangCode) {
        this.setLang(langCode)
    }
    setLang = (langCode: LangCode): void => {
        if (!(langCode in table)) {
            console.error(`language code ${langCode} doesn't exists in Language Table.`)
            return
        }
        this.data = table[langCode]
    }
    /**
     * # select language
     */
    get selectLang(): string {
        return this.data.selectLang
    }
    /**
     * used for login button
     */
    get login(): string {
        return this.data.login
    }
    /**
     * pop up greeting message
     */
    get hello(): string {
        return this.data.hello
    }
}
