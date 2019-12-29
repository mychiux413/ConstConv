
from __future__ import absolute_import
from create_multi_langs.composition.csv_reader import CSVReader
from create_multi_langs.composition.templater import Templater
from typing import NoReturn


class CreaterBase:
    def __init__(self, csv_file: str, output_code_file: str,
                 comment_head_prefix: str,
                 comment_tail_prefix: str,
                 comment_mid_prefix: str,
                 template_path: str):
        self._reader = CSVReader(csv_file)
        self._output = output_code_file
        self._templater = Templater(
            comment_head_prefix,
            comment_tail_prefix,
            comment_mid_prefix,
            template_path,
        )

    def render_data(self) -> dict:
        raise NotImplementedError()

    def render(self) -> str:
        return self._templater.render(self.render_data())

    def __call__(self) -> NoReturn:
        file_content = self.render()
        with open(self._output, 'w+', encoding='utf8') as f:
            f.write(file_content)
