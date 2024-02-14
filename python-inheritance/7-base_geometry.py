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
        if not isinstance(name, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
