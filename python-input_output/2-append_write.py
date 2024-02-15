#!/usr/bin/python3
"""holberton mandatory doc"""


def append_write(filename="", text=""):
    """holberton mandatory doc"""
    with open(filename, 'a', encoding='utf-8') as fd:
        bytes_written = fd.write(text)
    return bytes_written
