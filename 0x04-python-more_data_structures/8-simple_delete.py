#!/usr/bin/python3
""" function that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):
    """ function that deletes a key in a dictionary. """

    if a_dictionary.get(key):
        del a_dictionary[key]

    return (a_dictionary)
