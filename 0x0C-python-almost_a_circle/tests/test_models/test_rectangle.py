#!/usr/bin/python3
"""Defining a unittest for models/rectangle.py"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from contextlib import redirect_stdout


class testRectangle(unittest.TestCase):
    """Defining a unittest class"""
    def test_rectangle_is_base(self):
        """Testing whether rectangle is an instance of Base"""
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Base)

    def test_zero_arg(self):
        """Testing when no argument is passed to Rectangle"""
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_one_arg(self):
        """Testing when one argument is passed to Rectangle"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)

    def test_two_args(self):
        """Testing when two arguments are passed to Rectangle"""
        r2 = Rectangle(1, 1)
        r3 = Rectangle(2, 2)
        self.assertEqual(r2.id, r3.id - 1)

    def test_three_args(self):
        """Testing when three arguments are passed to Rectangle"""
        r4 = Rectangle(1, 2, 3)
        r5 = Rectangle(2, 2, 2)
        self.assertEqual(r4.id, r5.id - 1)

    def test_four_args(self):
        """Testing when four arguments are passed to Rectangle"""
        r6 = Rectangle(1, 2, 3, 4)
        r7 = Rectangle(2, 2, 2, 4)
        self.assertEqual(r6.id, r7.id - 1)

    def test_five_args(self):
        """Testing when five arguments are passed to Rectangle"""
        r7 = Rectangle(1, 2, 3, 4, 5)
        r8 = Rectangle(2, 2, 2, 2, 5)
        self.assertEqual(r7.id, 5)

    def test_more_than_five_args(self):
        """Testing when more than five arguments are passed to Rectangle"""
        with self.assertRaises(TypeError):
            r9 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_attr(self):
        """Testing to check whether width is a private instance"""
        with self.assertRaises(AttributeError):
            r9 = Rectangle(5, 4, 3, 2, 1)
            print(r9.__width)

    def test_height_attr(self):
        """Testing to check whether height is a private instance"""
        with self.assertRaises(AttributeError):
            r9 = Rectangle(5, 4, 3, 2, 1)
            print(r9.__height)

    def test_x_attr(self):
        """Testing to check whether x is a private instance"""
        with self.assertRaises(AttributeError):
            r9 = Rectangle(5, 4, 3, 2, 1)
            print(r9.__x)

    def test_y_attr(self):
        """Testing to check whether y is a private instance"""
        with self.assertRaises(AttributeError):
            r9 = Rectangle(5, 4, 3, 2, 1)
            print(r9.__y)

    def test_width_getter(self):
        """Testing width getter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(r9.width, 5)

    def test_width_setter(self):
        """Testing width setter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        r9.width = 6
        self.assertEqual(r9.width, 6)

    def test_height_getter(self):
        """Testing height getter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(r9.height, 4)

    def test_height_setter(self):
        """Testing width setter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        r9.height = 6
        self.assertEqual(r9.height, 6)

    def test_x_getter(self):
        """Testing x getter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(r9.x, 3)

    def test_x_setter(self):
        """Testing x setter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        r9.x = 6
        self.assertEqual(r9.x, 6)

    def test_y_getter(self):
        """Testing y getter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(r9.y, 2)

    def test_y_setter(self):
        """Testing y setter"""
        r9 = Rectangle(5, 4, 3, 2, 1)
        r9.y = 6
        self.assertEqual(r9.y, 6)

    """
        WIDTH TESTING
    """

    def test_width_None(self):
        """Testing when width receives None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r10 = Rectangle(None, 4, 3, 2, 1)

    def test_width_bool(self):
        """Testing when width receives a boolean"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r10 = Rectangle(True, 4, 3, 2, 1)

    def test_width_float(self):
        """Testing when width receives a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r10 = Rectangle(5.4, 4, 3, 2, 1)

    def test_width_str(self):
        """Testing when width receives a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r10 = Rectangle("None", 4, 3, 2, 1)

    def test_width_list(self):
        """Testing when width receives a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            my_list = [1, 2]
            r10 = Rectangle(my_list, 4, 3, 2, 1)

    def test_width_set(self):
        """Testing when width receives a set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            my_set = {1, 2}
            r10 = Rectangle(my_set, 4, 3, 2, 1)

    def test_width_dict(self):
        """Testing when width receives a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            my_dict = {"x": 1, "y": 2}
            r10 = Rectangle(my_dict, 4, 3, 2, 1)

    def test_width_tuple(self):
        """Testing when width receives a tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            my_tuple = (1, 2)
            r10 = Rectangle(my_tuple, 4, 3, 2, 1)

    def test_width_negative(self):
        """Testing when width receives a negative int"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r10 = Rectangle(-5, 4, 3, 2, 1)

    def test_width_zero(self):
        """Testing when width receives zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r10 = Rectangle(0, 4, 3, 2, 1)

    """
       HEIGHT TESTING
    """

    def test_height_None(self):
        """Testing when height receives None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r10 = Rectangle(5, None, 3, 2, 1)

    def test_height_bool(self):
        """Testing when height receives a boolean"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r10 = Rectangle(5, True, 3, 2, 1)

    def test_height_float(self):
        """Testing when height receives a float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r10 = Rectangle(5, 4.5, 3, 2, 1)

    def test_height_str(self):
        """Testing when height receives a string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r10 = Rectangle(5, "None", 3, 2, 1)

    def test_height_list(self):
        """Testing when height receives a list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            my_list = [1, 2]
            r10 = Rectangle(5, my_list, 3, 2, 1)

    def test_height_set(self):
        """Testing when height receives a set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            my_set = {1, 2}
            r10 = Rectangle(5, my_set, 3, 2, 1)

    def test_height_dict(self):
        """Testing when height receives a dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            my_dict = {"x": 1, "y": 2}
            r10 = Rectangle(5, my_dict, 3, 2, 1)

    def test_height_tuple(self):
        """Testing when height receives a tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            my_tuple = (1, 2)
            r10 = Rectangle(5, my_tuple, 3, 2, 1)

    def test_height_negative(self):
        """Testing when height receives a negative int"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10 = Rectangle(5, -4, 3, 2, 1)

    def test_height_zero(self):
        """Testing when height receives zero"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10 = Rectangle(5, 0, 3, 2, 1)

    """
       X TESTING
    """

    def test_x_None(self):
        """Testing when x receives None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r10 = Rectangle(5, 4, None, 2, 1)

    def test_x_bool(self):
        """Testing when x receives a boolean"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r10 = Rectangle(5, 4, True, 2, 1)

    def test_x_float(self):
        """Testing when x receives a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r10 = Rectangle(5, 4, 3.4, 2, 1)

    def test_x_str(self):
        """Testing when x receives a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r10 = Rectangle(5, 4, "None", 2, 1)

    def test_x_list(self):
        """Testing when x receives a list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            my_list = [1, 2]
            r10 = Rectangle(5, 4, my_list, 2, 1)

    def test_x_set(self):
        """Testing when x receives a set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            my_set = {1, 2}
            r10 = Rectangle(5, 4, my_set, 2, 1)

    def test_x_dict(self):
        """Testing when x receives a dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            my_dict = {"x": 1, "y": 2}
            r10 = Rectangle(5, 4, my_dict, 2, 1)

    def test_x_tuple(self):
        """Testing when x receives a tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            my_tuple = (1, 2)
            r10 = Rectangle(5, 4, my_tuple, 2, 1)

    def test_x_negative(self):
        """Testing when x receives a negative int"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r10 = Rectangle(5, 4, -3, 2, 1)

    """
       Y TESTING
    """

    def test_y_None(self):
        """Testing when y receives None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r10 = Rectangle(5, 4, 3, None, 1)

    def test_y_bool(self):
        """Testing when y receives a boolean"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r10 = Rectangle(5, 4, 3, True, 1)

    def test_y_float(self):
        """Testing when y receives a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r10 = Rectangle(5, 4, 3, 2.3, 1)

    def test_y_str(self):
        """Testing when y receives a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r10 = Rectangle(5, 4, 3, "None", 1)

    def test_y_list(self):
        """Testing when y receives a list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            my_list = [1, 2]
            r10 = Rectangle(5, 4, 3, my_list, 1)

    def test_y_set(self):
        """Testing when y receives a set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            my_set = {1, 2}
            r10 = Rectangle(5, 4, 3, my_set, 1)

    def test_y_dict(self):
        """Testing when y receives a dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            my_dict = {"x": 1, "y": 2}
            r10 = Rectangle(5, 4, 3, my_dict, 1)

    def test_y_tuple(self):
        """Testing when y receives a tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            my_tuple = (1, 2)
            r10 = Rectangle(5, 4, 3, my_tuple, 1)

    def test_y_negative(self):
        """Testing when y receives a negative int"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r10 = Rectangle(5, 4, 3, -2, 1)

    """
       AREA METHOD TESTING
    """
    def test_area(self):
        """Testing area method"""
        r11 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(r11.area(), 20)

    def test_area_two_args(self):
        """Testing area method with two arguments"""
        r11 = Rectangle(5, 4)
        self.assertEqual(r11.area(), 20)

    """
       DISPLAY METHOD TESTING
    """
    def test_display_two_args(self):
        """Testing display method with two arguments"""
        r11 = Rectangle(2, 2)
        s_out = StringIO()
        with redirect_stdout(s_out):
            r11.display()
        self.assertEqual(s_out.getvalue(), "##\n##\n")

    def test_display(self):
        """Testing display method"""
        r11 = Rectangle(3, 2, 1, 0)
        s_out = StringIO()
        with redirect_stdout(s_out):
            r11.display()
        self.assertEqual(s_out.getvalue(), " ###\n ###\n")

    """
       STR METHOD TESTING
    """
    def test_str(self):
        """Testing string method"""
        r11 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(str(r11), '[Rectangle] (1) 3/2 - 5/4')

    def test_str_two_args(self):
        """Testing string method with two arguments"""
        r11 = Rectangle(5, 4)
        self.assertEqual(str(r11), "[Rectangle] ({}) 0/0 - 5/4".format(r11.id))

    """
       UPDATE METHOD TESTING
    """
    def test_update(self):
        """Testing update method"""
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] ({}) 10/10 - 10/10'.format(r.id))
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (89) 4/5 - 2/3')
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), '[Rectangle] (89) 1/3 - 4/2')

    """
       TO DICTIONARY METHOD TESTING
    """
    def test_to_dictionary(self):
        """Testing dictionary method"""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r), '[Rectangle] ({}) 1/9 - 10/2'.format(r.id))
        self.assertEqual(r.to_dictionary(), {'x': 1, 'y': 9, 'id': 10, \
'height': 2, 'width': 10})
