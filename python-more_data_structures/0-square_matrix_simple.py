#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = map(matrix, square_value)
    return new_matrix
        

def square_value(x):
    return x * x