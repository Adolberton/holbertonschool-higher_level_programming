#!/usr/bin/python3
"""Holberton mandatory doc"""

from json import dumps, loads


class Base:
    """Holberton mandatory doc"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dumps list"""
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + '.json', 'w') as fd:
            fd.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instance = cls(4, 1)
        if cls.__name__ == "Square":
            instance = cls(4)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        instance_list = []
        dict_list = []
        try:
            with open(cls.__name__ + '.json', 'r') as fd:
                dict_list = Base.from_json_string(fd.read())
            for dict in dict_list:
                instance_list.append(cls.create(**dict))
            return instance_list
        except FileNotFoundError:
            return instance_list
