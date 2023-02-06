#!/usr/bin/python3
"""Defining a module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """A method with private attributes: width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns rectangle desription: [Rectangle] <width>/<height>"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
