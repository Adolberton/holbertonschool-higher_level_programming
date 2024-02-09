#!/usr/bin/python3
""" this module define a class"""


class Rectangle:
    """ the class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__wildth = width
        self.__heingt = height
    @property
    def width(self):
        return self.__wildth
    @property
    def height(self):
        return self.__heingt
    @property.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__wildth = value
    @property.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
    
