#!/usr/bin/python3
"""holberton mandatory doc"""


def read_file(filename=""):
    """holberton mandatory doc"""
    with open(filename) as fd:
        for line in fd:
            print(line, end="")
