#!/usr/bin/python3
"""holberton mandatory doc"""


def read_file(filename=""):
    """holberton mandatory doc"""
    with open(filename, 'r', encoding='utf-8') as fd:
        text = fd.read()
        print(text)
