#!/usr/bin/python3
"""
    Defining a class module
"""

class MyList(list):
    """ Class Mylist inherits from list"""
    def print_sorted(self):
        """This function prints out a sorted list"""
        print(sorted(self)) 
