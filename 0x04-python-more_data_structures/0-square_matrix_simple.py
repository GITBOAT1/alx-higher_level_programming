#!/usr/bin/python3
"""Squared simple
"""


def square_matrix_simple(matrix=[]):
    mx1 = []
    mx2 = []
    count = 0
    for i in matrix:
        for a in range(0, len(i)):
            mx1.append(i[a] * i[a])
    mx2.append(mx1)
    return(mx2)
