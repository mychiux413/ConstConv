#!/usr/bin/env python
from __future__ import absolute_import
from create_multi_langs.creater.go import CreaterGo
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Running DeepSpeech inference.')
    parser.add_argument('--from_csv', required=True,
                        type=str, help='Generate script from csv')
    parser.add_argument('--to_file', required=True,
                        type=str, help='generate file path')
    parser.add_argument('--backend', type=bool, default=False,
                        help='Default is generate frontend script for js/ts')
    args = parser.parse_args()

    print(args)

    if args.to_file.endswith('.go'):
        _ = CreaterGo(args.from_csv, args.to_file)


if __name__ == "__main__":
    main()
