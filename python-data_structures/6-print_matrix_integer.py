#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if matrix:
        for i in matrix:
            k = 0
            for j in i:
                k += 1
                if k < len(i):
                    print("{:d}".format(j), end=" ")
                else:
                    print("{:d}".format(j), end="")
            print()
