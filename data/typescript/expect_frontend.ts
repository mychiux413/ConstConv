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

let target = table["zh-tw"]


class MultiLangs {
    /**
     * # select language
     */
    get SelectLang(): string {
        return target.SelectLang
    }
    /**
     * used for login button
     */
    get Login(): string {
        return target.Login
    }
    /**
     * pop up greeting message
     */
    get Hello(): string {
        return target.Hello
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
