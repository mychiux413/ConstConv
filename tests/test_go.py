from __future__ import absolute_import
from create_multi_langs.creater.go import CreaterGo
from . import CSV_FILE, GO_OUTPUT, GO_EXPECT_FILE, compare_file
import os


def test_create_go_file():
    cgo = CreaterGo.from_csv_file(CSV_FILE, GO_OUTPUT)
    cgo()
    compare_file(GO_EXPECT_FILE, GO_OUTPUT)
    os.remove(GO_OUTPUT)
