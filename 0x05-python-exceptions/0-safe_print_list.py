#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0;
    try:
        for i in my_list[0:x]:
            print("{}".format(i), end="")
            count += 1
    except IndexError:
        print()
    finally:
        print()
        return (count)
