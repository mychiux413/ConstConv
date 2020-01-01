from __future__ import absolute_import
from create_multi_langs.creater.typescript_frontend import CreaterTypeScriptFrontEnd  # noqa: E501


class CreaterTypeScriptBackEnd(CreaterTypeScriptFrontEnd):

    @staticmethod
    def from_csv_file(csv_file: str, output_code_file: str):
        assert output_code_file.endswith(".ts"), \
            "typescript filename must ends with .ts"
        creater = CreaterTypeScriptBackEnd(
            csv_file,
            output_code_file,
            comment_head_prefix="/ **",
            comment_tail_prefix=" * ",
            comment_mid_prefix=" */",
            template_path="data/typescript/template_backend.tmpl"
        )
        return creater

    @property
    def multi_langs_properties(self) -> str:
        outs = []
        for field, note in self._reader.field_notes().items():
            out = ''
            out += self._templater.spaces(1) + '/**\n'
            out += self._templater.spaces(1) + ' * {}\n'.format(
                note
            )
            out += self._templater.spaces(1) + ' */\n'
            out += self._templater.spaces(1) + 'get {}()'.format(
                field) + ': string {\n'
            out += self._templater.spaces(2) + 'return this.data.{}\n'.format(
                field)
            out += self._templater.spaces(1) + '}'
            outs.append(out)
        return '\n'.join(outs)
