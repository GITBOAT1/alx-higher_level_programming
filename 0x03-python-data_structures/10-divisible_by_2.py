#!/usr/bin/python3
""" Only by 2
"""


def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return(None)
    new = []
    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            new.append(True)
        else:
            new.append(False)
    return (new)
