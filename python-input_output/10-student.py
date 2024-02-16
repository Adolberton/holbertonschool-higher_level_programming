#!/usr/bin/python3
"""holberton mandatory doc"""


class Student:
    """holberton mandatory doc"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            new_dict = {}
            for key in attrs:
                new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__
