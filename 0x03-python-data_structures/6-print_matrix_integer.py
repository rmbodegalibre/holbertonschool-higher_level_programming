#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for col in range(len(row)):
            print(f"{row[col]}", end="")
            if col is not len(row) -1:
                print(" ", end="")
        print("")
