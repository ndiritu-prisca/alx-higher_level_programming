#!/usr/bin/python3
"""Defining unittest for models/base.py"""


import unittest
from models.base import Base


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
        self.assertEqual(b5.id, 4)
