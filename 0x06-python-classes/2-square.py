#!/usr/bin/bash
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square with a private instance attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
