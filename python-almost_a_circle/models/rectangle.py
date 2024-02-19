#!/usr/bin/python3
"""Holberton mandatory doc"""

from models.base import Base



class Rectangle(Base):
    """Holberton mandatory doc"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Holberton mandatory doc"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
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
    def width(self):
        pass
    @height.setter
    def height(self):
        pass
    @x.setter
    def x(self):
        pass
    @y.setter
    def y(self):
        pass