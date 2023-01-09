#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """  function that deletes keys with a specific
         value in a dictionary.
    """

    list_d = list(a_dictionary.items())
    for key, val in list_d:
        if val == value:
            del a_dictionary[key]
    return (a_dictionary)
