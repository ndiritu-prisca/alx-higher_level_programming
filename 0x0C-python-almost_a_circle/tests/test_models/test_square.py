#!/usr/bin/python3
"""Defining a unittest for models/square.py"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from contextlib import redirect_stdout


class testSquare(unittest.TestCase):
    """Defining a unittest class"""
    def test_square_is_base(self):
        """Testing whether square is an instance of Base"""
        s1 = Square(10)
        self.assertIsInstance(s1, Base)

    def test_square_is_rectangle(self):
        """Testing whether square is an instance of Rectangle"""
        s1 = Square(10)
        self.assertIsInstance(s1, Rectangle)

    def test_zero_arg(self):
        """Testing when no argument is passed to Square"""
        with self.assertRaises(TypeError):
            s2 = Square()

    def test_one_arg(self):
        """Testing when one argument is passed to Square"""
        s2 = Square(1)
        s3 = Square(2)
        self.assertEqual(s2.id, s3.id - 1)

    def test_two_args(self):
        """Testing when two arguments are passed to Square"""
        s4 = Square(1, 2)
        s5 = Square(2, 4)
        self.assertEqual(s4.id, s5.id - 1)

    def test_three_args(self):
        """Testing when three arguments are passed to Square"""
        s6 = Square(1, 2, 3)
        s7 = Square(3, 2, 1)
        self.assertEqual(s6.id, s7.id - 1)

    def test_four_args(self):
        """Testing when four arguments are passed to Square"""
        s8 = Square(1, 2, 3, 4)
        s9 = Square(2, 2, 2, 4)
        self.assertEqual(s8.id, s9.id)

    def test_more_than_four_args(self):
        """Testing when more than four arguments are passed to Square"""
        with self.assertRaises(TypeError):
            s9 = Square(1, 2, 3, 4, 5)

    def test_width_attr(self):
        """Testing to check whether width is a private instance"""
        with self.assertRaises(AttributeError):
            s9 = Square(5, 4, 3, 2)
            print(s9.__width)

    def test_height_attr(self):
        """Testing to check whether height is a private instance"""
        with self.assertRaises(AttributeError):
            s9 = Square(5, 4, 3, 2)
            print(s9.__height)

    def test_x_attr(self):
        """Testing to check whether x is a private instance"""
        with self.assertRaises(AttributeError):
            s9 = Square(5, 4, 3, 2)
            print(s9.__x)

    def test_y_attr(self):
        """Testing to check whether y is a private instance"""
        with self.assertRaises(AttributeError):
            s9 = Square(5, 4, 3, 2)
            print(s9.__y)

    """
       STR METHOD TESTING
    """
    def test_str(self):
        """Testing str method"""
        s11 = Square(5, 4, 3, 2)
        self.assertEqual(str(s11), '[Square] (2) 4/3 - 5')

    def test_str_two_args(self):
        """Testing str method with one argument"""
        s11 = Square(5)
        self.assertEqual(str(s11), "[Square] ({}) 0/0 - 5".format(s11.id))

    """
       GETTER & SETTER METHOD TESTING
    """
    def test_size_getter(self):
        """Testing getter method"""
        s11 = Square(5, 4, 3, 2)
        self.assertEqual(s11.width, 5)

    def test_size_setter(self):
        """Testing setter method"""
        s11 = Square(5)
        s11.size = 10
        self.assertEqual(s11.width, 10)

    """
       UPDATE METHOD TESTING
    """
    def test_update(self):
        """Testing update method"""
        s = Square(5)
        self.assertEqual(str(s), '[Square] ({}) 0/0 - 5'.format(s.id))
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (89) 3/4 - 2')
        s.update(id=5, size=2, x=1, y=3)
        self.assertEqual(str(s), '[Square] (5) 1/3 - 2')

    """
       TO DICTIONARY METHOD TESTING
    """
    def test_to_dictionary(self):
        """Testing dictionary method"""
        s = Square(10, 2, 1)
        self.assertEqual(str(s), '[Square] ({}) 2/1 - 10'.format(s.id))
        self.assertEqual(s.to_dictionary(), {'id': 9, 'x': 2, 'size': 10,
                                             'y': 1})
