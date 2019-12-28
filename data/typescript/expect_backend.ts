interface LangData {
    SelectLang: string
    Login: string
    Hello: string
}

type LangCode = "zh-tw" | "en"

type LangTable = {
    [code in LangCode]: LangData
}

const table: LangTable = {
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
    get SelectLang(): string {
        return this.data.SelectLang
    }
    /**
     * used for login button
     */
    get Login(): string {
        return this.data.Login
    }
    /**
     * pop up greeting message
     */
    get Hello(): string {
        return this.data.Hello
    }
}

