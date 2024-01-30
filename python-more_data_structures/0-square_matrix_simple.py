#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    def square(nb):
        return nb ** 2
    for line in matrix:
        new_matrix += list(map(square, line))
    return new_matrix
