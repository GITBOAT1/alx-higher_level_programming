#!/usr/bin/python3
"""function that returns a set of common elements in two sets
"""


def multiply_by_2(a_dictionary):
    """ function that returns a new dictionary with all values multiplied by 2"""

    new_dictionary = dict()

    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2

    return(new_dictionary)
