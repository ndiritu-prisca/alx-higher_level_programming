#!/usr/bin/python3
"""
    A module defining a function that prints a square.
    The function print_square(size) takes in only one argument.
    It then prints a square of 'size' with # character.
"""


def print_square(size):
    """
        A function that prints a square with # and raises any errors found.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
