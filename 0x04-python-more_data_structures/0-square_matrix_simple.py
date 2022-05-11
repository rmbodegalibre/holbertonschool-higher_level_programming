#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_2 = []
    
    for lst in matrix:
        new_lst = list([num**2 for num in lst])
        matrix_2.append(new_lst)
    
    return matrix_2
