#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = map(square_value, matrix)
    return new_matrix
        

def square_value(x):
    return x * x