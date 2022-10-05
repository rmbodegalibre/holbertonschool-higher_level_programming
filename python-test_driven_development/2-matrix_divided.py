#!/usr/bin/python3
"""
This program contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message:
    "matrix must be a matrix (list of lists) of integers/floats"
    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception with the message:
    "Each row of the matrix must have the same size"
    div must be a number (integer or float),
    otherwise raise a TypeError exception with the message:
    "div must be a number"
    div can’t be equal to 0,
    otherwise raise a ZeroDivisionError exception with the message:
    "division by zero"
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns a new matrix
    """

    if type(matrix) is not list or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
        return

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
            return

    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
                return
 
    lenght = len(matrix[0])
    for i in matrix:
        if len(i) is not lenght:
            raise TypeError("Each row of the matrix must have the same size")
            return

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
        return

    if div == 0:
        raise ZeroDivisionError("division by zero")
        return

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
