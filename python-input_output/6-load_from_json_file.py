#!/usr/bin/python3
"""holberton mandatory doc"""

import json


def load_from_json_file(filename):
    """holberton mandatory doc"""
    with open(filename) as fd:
        return json.load(filename)
