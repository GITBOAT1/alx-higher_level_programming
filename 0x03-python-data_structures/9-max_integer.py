#!/usr/bin/python3
""" find the max
"""


def mx(a, b):
    if a > b:
        return(a)
    else:
        return(b)


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    else:
        max = my_list[0]
        for i in range(1, len(my_list)):
            max = mx(max, my_list[i])
    return (max)
