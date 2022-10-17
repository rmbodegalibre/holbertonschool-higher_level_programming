#!/usr/bin/python3
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
