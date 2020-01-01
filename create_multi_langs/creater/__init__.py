import re


def replace_non_en(string: str, non_en_repl='_', ignore_case=True) -> str:
    if ignore_case:
        string = re.sub(r'[^a-z]', non_en_repl, string, flags=re.IGNORECASE)
    else:
        string = re.sub(r'[^a-z]', non_en_repl, string)
    return string


def to_upper(string: str, non_en_repl='_', ignore_case=True) -> str:
    return replace_non_en(string, non_en_repl, ignore_case).upper()


def split_camelcase(string: str, insert_between: str = '_') -> str:
    if not is_camelcase(string):
        return string
    return re.sub(r'([a-z])([A-Z])', r'\1' + insert_between + r'\2', string)


def to_lower(string: str, non_en_repl='_', ignore_case=True) -> str:
    return replace_non_en(string, non_en_repl, ignore_case).lower()


def is_camelcase(string: str) -> bool:
    return string.lower() != string and string.upper() != string


def is_const(string: str) -> bool:
    return string.upper() == string


def is_lower(string: str) -> bool:
    return string.lower() == string
