#!/usr/bin/python3
"""print Reverse
"""


def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    a = len(my_list) - 1
    for i in range(len(my_list)):
        print("{:d}".format(my_list[a]))
        a = a - 1
