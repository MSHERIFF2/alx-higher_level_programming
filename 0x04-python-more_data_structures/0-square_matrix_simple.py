#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqr = []
    for row in matrix:
        sqrs = [elem ** 2 for elem in row]
        sqr.append(sqrs)
    return sqr
