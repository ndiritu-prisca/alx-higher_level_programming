#!/usr/bin/python3
"""Defining a module"""


class Rectangle:
    """Defining a class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """A public instance method that returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """A public instance method that returns a rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Defining the print() representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        string = ""
        for j in range(self.__height):
            string += str(self.print_symbol) * self.__width
            if j is not self.__height - 1:
                string += "\n"
        return (string)

    def __repr__(self):
        """Returns a string representation of the rectangle in order to
        recreate a new instance by using eval()"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Prints message when an instance of a rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A method that returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """It returns a new Rectangle instance with width == height == size"""
        return (cls(size, size))
