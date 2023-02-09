#!/usr/bin/python3
"""Defining a function."""


def pascal_triangle(n):
    """
        A function that returns a list of lists of integers representing the
        Pascal’s triangle of n
    """
    if n <= 0:
        return []

    p_tri = [[1]]
    while len(p_tri) != n:
        col = p_tri[-1]
        row = [1]
        for i in range(len(col) - 1):
            row.append(col[i] + col[i + 1])
        row.append(1)
        p_tri.append(row)
    return p_tri
