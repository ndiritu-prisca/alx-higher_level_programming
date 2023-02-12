#!/usr/bin/python3
"""Defining a module"""


from models.base import Base


class Rectangle(Base):
    """Defining a class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of class Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """A method to retrieve private instance width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """A method that sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A method to retrieve private instance height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """A method that sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """A method to retrieve private instance x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """A method that sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """A method to retrieve private instance y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """A method that sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
