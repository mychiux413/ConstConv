

_table = {
    "zh-tw": {
        "select_lang": "繁體中文",
        "login": "登入",
        "hello": "您好,歡迎",
    },
    "en": {
        "select_lang": "English",
        "login": "Login",
        "hello": "Hello,Welcome",
    },
}


class MultiLangs:

    def __init__(self, lang):
        self.set_lang(lang)

    def set_lang(self, lang):
        self._data = _table.get(lang, "zh-tw")

    @property
    def select_lang(self):
        return self._data["select_lang"]

    @property
    def login(self):
        return self._data["login"]

    @property
    def hello(self):
        return self._data["hello"]
