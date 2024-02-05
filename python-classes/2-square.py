#!/usr/bin/python3
"""this script write a class Square that defines a square """


class Square:
    """this class defines a square"""
    def __init__(self, size=0):
        """init new square instance"""
        try:
            self.__size = size
        except TypeError("size must be an integer"):
            pass
        except ValueError("size must be >= 0"):
            pass
