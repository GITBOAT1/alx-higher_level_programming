#!/usr/bin/python3
"""Search and replace
"""


def search_replace(my_list, search, replace):
    c = 0
    my_list1 = list(my_list)
    for i in my_list1:
        if i == search:
            my_list1.remove(my_list1[i])
            my_list1.insert(c, replace)
        c += 1
    return(my_list1)
