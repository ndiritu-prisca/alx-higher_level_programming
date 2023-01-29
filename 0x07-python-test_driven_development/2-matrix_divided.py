#!/usr/bin/python3
"""
    A division module.
    The module has one function that divides all elements of a matrix.
    The function returns a list of floats or integers.
"""


def matrix_divided(matrix, div):
    """
        A function that divides elements in a matrix and raises errors if any.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers\
/floats")
    for sublist in matrix:
        for item in sublist:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if len(set(len(sublist) for sublist in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
