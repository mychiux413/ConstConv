package generated

type LangData struct {
	SelectLang string
	Login      string
	Hello      string
}

type LangCode = string

var table = make(map[LangCode]LangData)

const (
	ZHTW LangCode = "zh-tw"
	EN   LangCode = "en"
)

func init() {
	table[ZHTW] = LangData{
		SelectLang: "繁體中文",
		Login:      "登入",
		Hello:      "您好,歡迎",
	}
	table[EN] = LangData{
		SelectLang: "English",
		Login:      "Login",
		Hello:      "Hello,Welcome",
	}
}

func NewMultiLangs(langCode LangCode) LangData {
	return table[langCode]
}

func (l *LangData) SetLang(langCode LangCode) {
	*l = table[langCode]
}
