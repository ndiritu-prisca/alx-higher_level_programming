#!/usr/bin/python3
"""
    An addition module.
    It has an addition function that takes in integers or floats as arguments.
    The float values are typecatsed into ints and the sum of 2 ints is returned
"""


def add_integer(a, b=98):
    """
        A function that adds 2 integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
