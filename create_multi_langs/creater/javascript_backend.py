from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase


class CreaterJavaScriptBackEnd(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str, output_code_file: str):
        assert output_code_file.endswith(".js"), \
            "javascript filename must ends with .js"
        creater = CreaterJavaScriptBackEnd(
            csv_file,
            output_code_file,
            comment_head_prefix="/ **",
            comment_tail_prefix=" * ",
            comment_mid_prefix=" */",
            template_path="data/javascript/template_backend.tmpl"
        )
        return creater

    def render_data(self) -> dict:
        return {}
