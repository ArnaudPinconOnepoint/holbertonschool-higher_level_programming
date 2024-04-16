#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = matrix.copy()
    return list(map(lambda x: x**x, new_matrix))
