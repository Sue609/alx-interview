#!/usr/bin/python3
"""
pascal triangle function
"""

def pascal_triangle(n):
    """
    Function that returns a list of integers representing Pascal's triangle.
    """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n - 1)
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)
        return triangle
