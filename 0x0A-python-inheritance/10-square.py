#!/usr/bin/python3
"""Defining a module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle"""
    def __init__(self, size):
        """A method with a private attribute: size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of a rectangle"""
        return (self.__size * self.__size)

    def __str__(self):
        """Returns rectangle desription: [Rectangle] <width>/<height>"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
