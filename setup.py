#!/usr/bin/env python

from setuptools import setup, find_packages

description = \
""" Create-Multi-Langs is a library for creating code file from translated csv file.

features:

- Use CSV file grid table as translated source data instead of JSON to better manage translations.
- Output code language support python, go, javascript(ES6), typescript.
- No more map or dict like so, but use property to get code intelligence.
- Support watching mode for source csv file.

"""  # noqa: E501

with open('requirements.txt') as fid:
    requires = [line.strip() for line in fid]

setup(
    name='Create-Multi-Langs',
    version='0.1',
    description=description,
    author='Yihua Chiu',
    author_email='mychiux413@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['create-multi-langs=create_multi_langs.command_line:main'],  # noqa: E501
    },
    platforms="any",
    python_requires='>=3.5',
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Code Generator",
    ],
    install_requires=requires,
)
