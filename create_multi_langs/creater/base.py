
from __future__ import absolute_import
from create_multi_langs.composition.csv_reader import CSVReader
from create_multi_langs.composition.templater import Templater
from typing import NoReturn
import inspect


class CreaterBase:
    def __init__(self, csv_file: str, output_code_file: str,
                 template_path: str,
                 field_wrapper=lambda x: x,
                 sep=','):
        self._reader = CSVReader(csv_file, field_wrapper, sep)
        self._output = output_code_file
        self._templater = Templater(
            template_path,
        )

    def render_data(self) -> dict:
        out = {}
        for member_name, member in inspect.getmembers(self.__class__):
            if isinstance(member, property):
                out[member_name] = getattr(self, member_name)
        return out

    def render(self) -> str:
        return self._templater.render(self.render_data())

    def __call__(self) -> NoReturn:
        file_content = self.render().strip() + '\n'
        print('Generate Script at {}...'.format(self._output))
        with open(self._output, 'w+', encoding='utf8') as f:
            f.write(file_content)
