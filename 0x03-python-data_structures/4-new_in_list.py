#!/usr/bin/python3
"""Replace element
"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return(my_list)
    else:
        myList = my_list.copy()
        myList[idx] = element
        return(myList)
