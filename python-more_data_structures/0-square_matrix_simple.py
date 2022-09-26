#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        matrix2 = []
        row = 0
        col = 0
        for i in matrix:
            matrix2.append([])
            for j in i:
                matrix2[row].append(j ** 2)
                col += 1
            row += 1
            col = 0
        return matrix2
