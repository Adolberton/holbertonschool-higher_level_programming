#!/usr/bin/python3
"""Module with a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor (`div`)."""
    e = "matrix must be a matrix (list of lists) of integers/floats"
    def err(str):
        """raise the error"""
        if str == "list":
            raise TypeError(f"{e}")
        if str == "row":
            raise TypeError("Each row of the matrix must have the same size")
        if str == "div":
            raise TypeError("div must be a number")
        if str == "div0":
            raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        err("list")
    ref_size = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list)
            err("list")
        if len(row) != ref_size:
            err("row")
        for nb in row:
            if not isinstance(nb, (int, float)):
                err("list")
    if not isinstance(div, (int, float)):
        err("div")
    if div == 0:
        err("div0")

    matrix_divided = [[round((nb / div), 2) for nb in row] for row in matrix]
    return matrix_divided

matrix = [
    [-3.14159, -2.71828, -1.41421],
    [6.28318, -5.43656, -2.82843],
    [-9.42477, -8.15484, -4.24264]
]


print("Matrice d'origine :", matrix)
print("Matrice après opération :", matrix_divided(matrix, -2))
