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
    """
    Initializes a new Rectangle instance.

    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle.

    Methods:
        __init__(width, height): Initializes a new Rectangle
        instance with the specified width and height.
    """


    def __init__(self, width, height):
        """
        Initialize the new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """


        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
