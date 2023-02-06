#!/usr/bin/python3
"""
    Defining a lookup method.
    It return a list of all available attributes and methods of an object
    The function does not have any attributes
"""


def lookup(obj):
    """
        A function that returns a list of attributes and methods of an object
    """
    return (list(dir(obj)))
