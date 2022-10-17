#!/usr/bin/python3
"""
File: 12-pascal_triangle.py - Create a function def pascal_triangle(n): that
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    pascal_triangle - returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    if n <= 0:
        return []

    p_t = [[1]]
    while len(p_t) != n:
        tri = p_t[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        p_t.append(tmp)
    return p_t
