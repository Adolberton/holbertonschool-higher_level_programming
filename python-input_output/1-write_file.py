#!/usr/bin/python3
"""holberton mandatory doc"""


def write_file(filename="", text=""):
    """holberton mandatory doc"""
    with open(filename, 'w', encoding='utf-8') as fd:
        fd.write(text)
