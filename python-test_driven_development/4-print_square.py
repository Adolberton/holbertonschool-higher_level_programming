#!/usr/bin/python3
"""supercomment"""


def print_square(size):
    """supercomment"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
