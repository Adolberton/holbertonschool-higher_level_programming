#!/usr/bin/python3
"""this script write a class Square that defines a square """


class Square:
    """this class defines a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.size > 0:
            for i in range(self.size):
                print("#" * self.size)
        else:
            print()
