#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for n in my_string:
        if n == 'c' or n == 'C':
            continue
        new_str += n
    return new_str
