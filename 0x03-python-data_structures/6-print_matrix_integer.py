#!/usr/bin/python3
"""
This script is used to print a matrix of integers.

Author: Ricardo Montaña
Date: 9-05-2022
"""

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col < len(matrix[row]) - 1:
                    print(matrix[row][col], end=" ")
                else:
                    print(matrix[row][col], end="")
            print()
