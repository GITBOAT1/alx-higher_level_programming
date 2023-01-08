#!/usr/bin/python3
"""function that returns a set of common elements in two sets
"""


def only_diff_elements(set_1, set_2):
    """ element presen in one set """

    return (set_1 ^ set_2)
