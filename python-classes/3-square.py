#!/usr/bin/python3
"""this script write a class Square that defines a square """


class Square:
    """this class defines a square"""
    def area(self):
        """init new square instance"""
    def __init__(self, size=0):
        """init new square instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
