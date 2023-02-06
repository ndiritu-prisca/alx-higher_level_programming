#!/usr/bin/python3
"""
    Defining a class module with one method
    The class module inherits form a list object
    The public instance methos prints a sorted list
"""

class MyList(list):
    """ Class Mylist inherits from list"""
    def print_sorted(self):
        """This function prints out a sorted list"""
        print(sorted(self)) 
