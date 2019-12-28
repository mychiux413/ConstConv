from __future__ import absolute_import
import jinja2


class Templater:

    def __init__(self,
                 comment_head_prefix: str,
                 comment_tail_prefix: str,
                 comment_mid_prefix: str,
                 template_path: str):
        self._comment_head_prefix: str = comment_head_prefix
        self._comment_tail_prefix: str = comment_tail_prefix
        self._comment_mid_prefix: str = comment_mid_prefix
        self._template_content = open(template_path, 'r').read()

    def comment(self, contents: str, n_spaces: int = 0) -> str:
        spaces = " " * n_spaces
        out = ""
        out += spaces + self._comment_head_prefix + "\n"
        for content in contents.split("\n"):
            out += spaces + self._comment_mid_prefix + content + "\n"
        out += spaces + self._comment_tail_prefix + "\n"

        return out

    def key_value_lines(self,
                        key_values: dict,
                        double_quote_key: bool = False,
                        split_punctuation: str = ": ",
                        end_punctuation: str = "",
                        n_spaces: int = 0) -> str:
        spaces = " " * n_spaces
        double_quotes = '"' if double_quote_key else ''
        out = ""
        for key, value in key_values.items():
            out += '''{spaces}{double_quotes}{key}{double_quotes}{split_punctuation}"{value}"{end_punctuation}\n'''.format(  # noqa: E501
                spaces=spaces,
                double_quotes=double_quotes,
                key=key,
                split_punctuation=split_punctuation,
                value=value,
                end_punctuation=end_punctuation
            )

        return out

    def render(self, data: dict) -> str:
        t = jinja2.Template(self._template_content)
        return t.render(**data)