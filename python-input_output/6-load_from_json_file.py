#!/usr/bin/python3
"""holberton mandatory doc"""

import json


def load_from_json_file(filename):
    """holberton mandatory doc"""
    with open(filename) as fd:
        py_obj = json.load(filename)
        return py_obj
