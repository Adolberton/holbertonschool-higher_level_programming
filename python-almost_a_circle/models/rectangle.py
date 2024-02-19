#!/usr/bin/python3
"""Holberton mandatory doc"""

from models.base import Base



class Rectangle(Base):
    """Holberton mandatory doc"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Holberton mandatory doc"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if value <= 0:
            raise TypeError("height must be > 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    @x.setter
    def x(self, value):
        if value < 0:
            raise TypeError("x must be >= 0")
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value
    @y.setter
    def y(self, value):
        if value < 0:
            raise TypeError("y must be >= 0")
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__y = value
