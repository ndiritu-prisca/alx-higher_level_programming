#!/usr/bin/python3
"""Defining unittest for models/base.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class testBase(unittest.TestCase):
    """Defining a unittest class"""
    def test_no_arg(self):
        """Testing when no argument is passed"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_other_no_arg(self):
        """Testing when an additional no argument is passed"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_one_arg(self):
        """Testing when one argument is passed"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_two_no_arg(self):
        """Testing when two no arguments are passed"""
        b4 = Base()
        b5 = Base()
        self.assertEqual(b4.id, b5.id - 1)

    """
        TO JSON STRING METHOD TESTING
    """
    def test_to_json_string(self):
        """Testing to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 4, "width": 10, \
"height": 7, "x": 2, "y": 8}]')

    """
        SAVE TO FILE CLASS METHOD TESTING
    """
    def test_save_to_file(self):
        """Testing save_to_file class method"""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 3, "width": 10, "height": 7, \
"x": 2, "y": 8}]')

    """
        FROM JSON STRING METHOD TESTING
    """
    def test_from_json_string(self):
        """Testing from_json_string method"""
        list_input = [{'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'id': 7, 'width': 1, 'height': 7}])
