#!/usr/bin/python3
""" remove character
"""


def no_c(my_string):
    load = str()
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            load = load + my_string[i]
    return(load)
