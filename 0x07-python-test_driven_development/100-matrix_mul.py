#!/usr/bin/python3
"""
    A matrices multiplication module
    The function takes in two matrices and returns the product
    Values in the matrices must either be integers or floats
"""


def matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for sublist in m_a:
        for item in sublist:
            if type(item) is not int and type(item) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for sublist in m_b:
        for item in sublist:
            if type(item) is not int and type(item) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(set(len(sublist) for sublist in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(sublist) for sublist in m_a)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return (result)
