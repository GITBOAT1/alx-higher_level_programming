#!/usr/bin/python3
"""Search and replace
"""


def search_replace(my_list, search, replace):
    """ search and replace """

    new_list = [i if i != search else replace for i in my_list]
    return (new_list)
