#!/usr/bin/python3
"""Defining a module"""


from models.base import Base


class Rectangle(Base):
    """Defining a class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of class Rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
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

    def area(self):
        """
            A public method that returns the area value of the Rectangle
            instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
            A public method that prints in stdout the Rectangle instance
            with the character #
        """
        for n in range(self.__y):
            print()
        for b in range(self.__height):
            [print(" ", end="") for m in range(self.__x)]
            for a in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
            This method returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height))

    def update(self, *args, **kwargs):
        """
            A public method that assigns a key/value argument to attributes:
            **kwargs must be skipped if *args exists and is not empty
            1st argument should be the id attribute,
            2nd argument should be the width attribute,
            3rd argument should be the height attribute,
            4th argument should be the x attribute,
            5th argument should be the y attribute.
        """
        num_args = len(args)
        if num_args > 0:
            self.id = args[0]
        if num_args > 1:
            self.width = args[1]
        if num_args > 2:
            self.height = args[2]
        if num_args > 3:
            self.x = args[3]
        if num_args > 4:
            self.y = args[4]
        if num_args == 0:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """This method returns the dictionary representation of a Rectangle"""
        my_dict = {"id": self.id, "width": self.width, "height": self.height,
                   "x": self.x, "y": self.y}
        return (my_dict)
