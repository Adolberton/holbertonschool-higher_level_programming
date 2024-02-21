#!/usr/bin/python3
"""Holberton mandatory doc"""

from json import dumps


class Base:
    """Holberton mandatory doc"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)
