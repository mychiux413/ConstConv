# Create-Multi-Langs

Create-Multi-Langs is a package to create code for multi-lingual sites development, 

### Features
- Use CSV file grid table as translated source data instead of JSON to better manage translations.
- Output code language support python, go, javascript(ES6), typescript.
- No more map or dict like so, but use property to get `code intelligence`.
- Support watching mode for source csv file.

### Install
```
pip install create-multi-langs
```


### Prepare Data

prepare csv data by yourself, liek `valid_format.csv`
|_field | zh-tw | en | _note |
|---|---|---|---|
|SelectLang|繁體中文|English|# select language|
|Login|登入|Login|used for login button|
|Hello|您好,歡迎|Hello,Welcome|pop up greeting message|

- Use CSV file as source data, a grid table is easier to manage for multi-lingual application.
- `_field` and `_note` are preserved column names, others column names are considered as language code
- the values under column `_field`, will become the field name in code file, but constraint the name with common naming rule of which language
- the values under column `_note`, will become the comment for code docs

### usage
```
create-multi-langs valid_format.csv generated.py
```
- support output language: `typscript`, `javascript`, `go`, `python`
- language determined by your output filename extension like: .py .go .js .ts .mjs

### import from generated.py
```
from generated import MultiLangs, ZH_TW, EN

ml = MultiLangs(ZH_TW)
assert ml.hello == "您好,歡迎"
assert ml.login == "登入"
assert ml.select_lang == "繁體中文"

ml.set_lang(EN)
assert ml.hello == "Hello,Welcome"
assert ml.login == "Login"
assert ml.select_lang == "English"
```

### help
```
$ create-multi-langs --help
usage: create-multi-langs [-h] [--backend] [--py_typing] [--watch] [--sep SEP]
                          [--naming_rule NAMING_RULE]
                          from_csv to_file

Running DeepSpeech inference.

positional arguments:
  from_csv              Generate script from csv
  to_file               generate file path, support ext: .go .py .js .ts .mjs

optional arguments:
  -h, --help            show this help message and exit
  --backend, -b         Default is generate frontend script for js/ts
  --py_typing, -t       Default is generate python script without typing
  --watch, -w           Watch csv file changed
  --sep SEP, -s SEP     CSV seperated punctuation
  --naming_rule NAMING_RULE, -n NAMING_RULE
                        specify your property style, [valid options]
                        `ucc`(UpperCamelCase), `lcc`(lowerCamelCase),
                        `upper`(ALL_UPERCASE_UNDERSCORE),
                        `lower`(all_lowercase_underscore) [default setting]
                        Go: `ucc`, Python: `lower`, Typescript: `lcc`,
                        javascript: `lcc`
```