#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class.
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Methods:
        area(self): raises an exception with a message
                    indicating that the method is not implemented.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
