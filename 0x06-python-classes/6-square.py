#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with a private instance attribute"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position."""
        return (self.__size)

    @position.setter
    def position(self, value):
        """Sets the position and if value is not a tuple it raises an error"""
        if (type(value) is not tuple or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value) or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the char #, newline if size=0"""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]
            for x in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                for y in range(self.__size):
                    print("#", end="")
                print()
