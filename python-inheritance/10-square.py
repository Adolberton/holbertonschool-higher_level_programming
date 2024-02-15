#!/usr/bin/python3

"""
This module defines 'the Square` class and the `Rectangle` class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initializes a new  instance."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
