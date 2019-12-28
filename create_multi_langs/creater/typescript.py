from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase


class CreaterTypeScript(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str, output_code_file: str):
        assert output_code_file.endswith(".ts"), \
            "typescript filename must ends with .ts"
        creater = CreaterTypeScript(
            csv_file,
            output_code_file,
            comment_head_prefix="/ **",
            comment_tail_prefix=" * ",
            comment_mid_prefix=" */",
            template_path="data/typescript/template.tmpl"
        )
        return creater

    def render_data(self) -> dict:
        return {}
