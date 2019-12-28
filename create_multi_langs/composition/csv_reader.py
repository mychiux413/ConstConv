from __future__ import absolute_import
import pandas as pd
from typing import List


class CSVReader:
    def __init__(self, csv_file: str):
        self._df: pd.DataFrame = pd.read_csv(csv_file)
        self._PRESERVED_COLUMN_NAMES: List[str] = ["_key", "_note"]

    def default_lang_code(self) -> str:
        return ""
