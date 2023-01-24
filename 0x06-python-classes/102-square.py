#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square with a private instance attribute"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of square if value is an int and is greater that 0"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Defines == comparison to a square"""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Defines != comparison to a square"""
        return (self.area() != other.area())

    def __gt__(self, other):
        """Defines > comparison to a square"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Defines >= comparison to a square"""
        return (self.area() >= other.area())

    def __lt__(self, other):
        """Defines < comparison to a square"""
        return (self.area() < other.area())

    def __le__(self, other):
        """Defines <= comparison to a square"""
        return (self.area() <= other.area())
