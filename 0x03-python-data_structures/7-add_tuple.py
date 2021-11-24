#!/usr/bin/python3
"""Tupple Adding
"""


def add_tuple(tuple_a=(), tuple_b=()):
    ze = (0,)

    while(len(tuple_a) < 2):
        tuple_a += ze
    while(len(tuple_b) < 2):
        tuple_b += ze
    tup = list(tuple_a)
    tup1 = list(tuple_b)
    for i in range(0, (len(tuple_a) - 1)):
        tup[i] = (tup[i] + tup1[i])
    ze = tuple(tup)
    return(ze)
