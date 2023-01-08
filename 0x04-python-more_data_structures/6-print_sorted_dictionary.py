#!/usr/bin/python3
"""a function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    """ a function that prints a dictionary by ordered keys."""

    if a_dictionary:
        for key, val in sorted(a_dictionary.items()):
            print("{}: {}".format(key, val))
