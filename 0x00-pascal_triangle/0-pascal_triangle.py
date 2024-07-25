#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for row in range(1, n):
        new_row = [1]
        previous_row = triangle[-1]
        new_row += [previous_row[i] + previous_row[i + 1] for i in range(len(previous_row) - 1)]
        new_row.append(1)
        triangle.append(new_row)
    return triangle
