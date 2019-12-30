#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Create Multi Langs',
    version='0.1',
    description='Create Multi Langs',
    author='Yihua Chiu',
    author_email='mychiux413@gmail.com',
    # package_dir={'create_multi_langs': '.'},
    packages=find_packages(),
    entry_points={
        'console_scripts': ['create-multi-langs=create_multi_langs.command_line:main'],  # noqa: E501
    }
)
