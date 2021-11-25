#!/usr/bin/python3
"""Unique addition
"""


def uniq_add(my_list=[]):
    uni = set(my_list)
    un = list(uni)
    li = 0
    for i in range(len(un)):
        li += un[i]
    return(li)
