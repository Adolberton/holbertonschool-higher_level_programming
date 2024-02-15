#!/usr/bin/python3
"""holberton mandatory doc"""

import json


def save_to_json_file(my_obj, filename):
    """holberton mandatory doc"""
    with open(filename, 'w') as fd:
        return json.dump(my_obj, fd)
