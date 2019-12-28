CSV_FILE = "data/valid_format.csv"
GO_OUTPUT = "tests/go/generated.go"
GO_EXPECT_FILE = "data/go/expect.go"
PYTHON_OUTPUT = "tests/python/generated.py"
PYTHON_EXPECT_FILE = "data/python/expect.py"
PYTHON_TYPING_OUTPUT = "tests/python/generated_typing.py"
PYTHON_EXPECT_TYPING_FILE = "data/python/expect_typing.py"
TYPESCRIPT_OUTPUT = "tests/typescript/generated.ts"
TYPESCRIPT_EXPECT_FILE = "data/typescript/expect.ts"
JAVASCRIPT_OUTPUT = "tests/javascript/generated.js"
JAVASCRIPT_EXPECT_FILE = "data/javascript/expect.js"


def compare_file(expect_file: str, result_file: str):
    expects = open(expect_file, 'r', encoding='utf8').read().split('\n')
    results = open(result_file, 'r', encoding='utf8').read().split('\n')
    err = ""
    for i, expect in enumerate(expects):
        try:
            if results[i] != expect:
                err += "[Different LINE {}] expect v.s. result:\n'{}'\n'{}'\n".format(  # noqa E501
                    i+1, expect, results[i]
                )
        except IndexError:
            err += "[Different File Lines] expect: {}, but got {}\n".format(
                len(expects), len(results)
            )
            break

    assert not err, err
