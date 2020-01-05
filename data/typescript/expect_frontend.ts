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

let target = table["zh-tw"]


class MultiLangs {
    /**
     * # select language
     */
    get selectLang(): string {
        return target.selectLang
    }
    /**
     * used for login button
     */
    get login(): string {
        return target.login
    }
    /**
     * pop up greeting message
     */
    get hello(): string {
        return target.hello
    }
}

/**
 * @param langCode  set to change instance `ml`'s language 
 */
export const setLang = (langCode: LangCode): void => {
    if (!(langCode in table)) {
        console.error(`language code ${langCode} doesn't exists in Language Table.`)
        return
    }
    target = table[langCode]
}

/**
 * use instance `ml` to get language content which you've set from csv file before
 * use `setLang(<LanguageCode>)` to change the language you want
 */
export const ml = new MultiLangs()
