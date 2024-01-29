#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for num in col:
            print("{:d}".format(num), end=" ")
        print("")
