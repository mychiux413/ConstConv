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

ZH_TW = "zh-tw"
EN = "en"


class MultiLangs:

    def __init__(self, lang_code):
        """Create MultiLangs with specified `language code`
        ### Valid Lang Codes
        - "zh-tw"
        - "en"
        """
        self.set_lang(lang_code)

    def set_lang(self, lang_code):
        """set_lang set language code inplace"""
        new_data = _table.get(lang_code)
        if new_data is None:
            print("[error] invalid lang code: {}".format(lang_code))
            print("lang code must be in: {}".format(
                _table.keys()
            ))
            return
        self._data = new_data

    @property
    def select_lang(self):
        """# select language"""
        return self._data["select_lang"]

    @property
    def login(self):
        """used for login button"""
        return self._data["login"]

    @property
    def hello(self):
        """pop up greeting message"""
        return self._data["hello"]
