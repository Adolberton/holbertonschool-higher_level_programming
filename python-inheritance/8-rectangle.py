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
        if type(value) is not (int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """bla bla bla bla"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
