#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defining unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Testing an ordered list of integers."""
        ordered = [4, 5, 6, 7]
        self.assertEqual(max_integer(ordered), 7)

    def test_unordered_list(self):
        """Testing an unordered list of integers."""
        unordered = [4, 7, 10, 8]
        self.assertEqual(max_integer(unordered), 10)

    def test_empty_list(self):
        """Testing an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Testing a list with a single element."""
        one_elem = [9]
        self.assertEqual(max_integer(one_elem), 9)

    def test_floats(self):
        """Testing a list of floats."""
        floats = [2.54, 8.53, -7.132, 13.1, 4.0]
        self.assertEqual(max_integer(floats), 13.1)

    def test_equal_ints(self):
        """Testing a list of integers and floats."""
        ints_and_floats = [12, 1, 12, 1, 6]
        self.assertEqual(max_integer(ints_and_floats), 12)

    def test_string(self):
        """Testing a string."""
        string = "Horbeton"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        """Testing a list of strings."""
        strings = ["Horbeton", "and", "ALX"]
        self.assertEqual(max_integer(strings), "and")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
