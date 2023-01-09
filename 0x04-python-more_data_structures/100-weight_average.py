#!/usr/bin/python3
"""function that returns a set of common elements in two sets
"""


def weight_average(my_list=[]):
    """ unction that returns the weighted average of all
        integers tuple
    """

       if my_list:
           res = sum(a * b for a, b in my_list) / sum(b for a, b in my_list))
           return (res)

    return(0)
