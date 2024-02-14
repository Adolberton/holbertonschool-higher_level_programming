#!/usr/bin/python3

"""
Module with an empty class `BaseGeometry`.
"""


class BaseGeometry:
    """
    Defines the BaseGeometry class.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise Exception(TypeError("<name> must be an integer"))
        if value <= 0:
            raise Exception(ValueError("<name> must be greater than 0"))
