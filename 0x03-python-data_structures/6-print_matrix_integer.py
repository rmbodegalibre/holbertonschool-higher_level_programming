#!/usr/bin/python3
"""
This script is used to print a matrix of integers.

Author: Ricardo Montaña
Date: 9-05-2022
"""

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for col in range(len(row)):
                print(f"{row[col]}", end="")
                if col is not len(row) -1:
                    print(" ", end="")
            print("")
