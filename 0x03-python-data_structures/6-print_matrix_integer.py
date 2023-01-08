#!/usr/bin/python3
"""Lists of lists
"""


def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        print(' '.join(["{:d}".format(elem) for elem in row]))
