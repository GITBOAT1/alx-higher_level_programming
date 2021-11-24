#!/usr/bin/python3
"""Squared simple
"""


def square_matrix_simple(matrix=[]):
    mx2 = []
    count = 0
    for i in matrix:
        mx1 = []
        for a in range(0, len(i)):
            mx1.append(i[a] * i[a])
        mx2.insert(count, mx1)
        count += 1
    return(mx2)
