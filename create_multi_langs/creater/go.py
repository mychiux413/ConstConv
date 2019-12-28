from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase
import os


class CreaterGo(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str, output_code_file: str):
        assert output_code_file.endswith(".go"), \
            "go filename must ends with .go"
        creater = CreaterGo(
            csv_file,
            output_code_file,
            comment_head_prefix="",
            comment_tail_prefix="",
            comment_mid_prefix="// ",
            template_path="data/go/template.tmpl"
        )
        return creater

    @property
    def lang_data_contents(self) -> str:
        return ""

    @property
    def lang_code_contents(self) -> str:
        return ""

    @property
    def init_contents(self) -> str:
        return ""

    @property
    def package_name(self) -> str:
        return os.path.splitext(os.path.basename(self._output))[0]

    def render_data(self) -> dict:
        return {
            "lang_data_contents": self.lang_data_contents,
            "lang_code_contents": self.lang_code_contents,
            "init_contents": self.init_contents,
            "package_name": self.package_name,
        }
