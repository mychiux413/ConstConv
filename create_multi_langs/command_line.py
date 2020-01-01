#!/usr/bin/env python
from __future__ import absolute_import
from create_multi_langs.creater.go import CreaterGo
from create_multi_langs.creater.python import CreaterPython
from create_multi_langs.creater.python_typing import CreaterPythonTyping
from create_multi_langs.creater.typescript_backend import CreaterTypeScriptBackEnd  # noqa: E501
from create_multi_langs.creater.typescript_frontend import CreaterTypeScriptFrontEnd  # noqa: E501
from create_multi_langs.creater.javascript_backend import CreaterJavaScriptBackEnd  # noqa: E501
from create_multi_langs.creater.javascript_frontend import CreaterJavaScriptFrontEnd  # noqa: E501
import argparse
import time
import os
import sys

VALID_EXTS = ['.py', '.go', '.ts', '.js']


def main():
    parser = argparse.ArgumentParser(
        description='Running DeepSpeech inference.')
    parser.add_argument('--from_csv', required=True,
                        type=str, help='Generate script from csv')
    parser.add_argument('--to_file', required=True,
                        type=str, help='generate file path')
    parser.add_argument('--backend', action='store_true',
                        help='Default is generate frontend script for js/ts')
    parser.add_argument('--py_typing', action='store_true',
                        help='Default is generate python script without typing')  # noqa: E501
    parser.add_argument('--watch', action='store_true',
                        help='Watch csv file changed')
    args = parser.parse_args()

    args.from_csv = os.path.abspath(args.from_csv)
    args.to_file = os.path.abspath(args.to_file)
    assert os.path.exists(args.from_csv), \
        "The csv file `{}` doesn't exists".format(args.from_csv)
    assert os.path.splitext(args.to_file)[1] in VALID_EXTS, \
        "The extension filename must be in " + str(VALID_EXTS)

    if os.path.exists(args.to_file):
        print('[WARNING] the to_file `{}` already exists'.format(
            args.to_file) +
            ', and will be overwritten.')

    if args.watch:
        try:
            print('[Enable Watching Mode]')
            print('[From CSV File] {}'.format(args.from_csv))
            print('[To File] {}'.format(args.to_file))
            last_mtime = os.stat(args.from_csv).st_mtime
            while True:
                time.sleep(0.5)
                current_mtime = os.stat(args.from_csv).st_mtime
                if current_mtime != last_mtime:
                    print('Detect csv file changed...')
                    _generate(args)
                    last_mtime = current_mtime
        except KeyboardInterrupt:
            print('Stop watching')
            sys.exit(0)

    if os.path.exists(args.to_file):
        print('Overwrite (y/n)?')
        yes_no = input().lower()
        if yes_no != "y":
            print('Abort program')
            sys.exit(0)

    _generate(args)


def _generate(args: argparse.Namespace):
    to_file = args.to_file
    if to_file.endswith('.go'):
        from_csv_file = CreaterGo.from_csv_file
    elif to_file.endswith('.py'):
        if args.py_typing:
            from_csv_file = CreaterPythonTyping.from_csv_file
        else:
            from_csv_file = CreaterPython.from_csv_file
    elif to_file.endswith('.ts'):
        if args.backend:
            from_csv_file = CreaterTypeScriptBackEnd.from_csv_file
        else:
            from_csv_file = CreaterTypeScriptFrontEnd.from_csv_file
    elif to_file.endswith('.js'):
        if args.backend:
            from_csv_file = CreaterJavaScriptBackEnd.from_csv_file
        else:
            from_csv_file = CreaterJavaScriptFrontEnd.from_csv_file
    else:
        raise argparse.ArgumentError(
            "must set to_file as .go .py .ts or .js, but got {}".format(
                to_file
            ))
    creater = from_csv_file(args.from_csv, to_file)
    creater()


if __name__ == "__main__":
    main()
