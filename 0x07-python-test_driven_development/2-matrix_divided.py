#!/usr/bin/python3
"""

Divide a matrix

"""


def matrix_divided(matrix, div):
    """ this  this function divide """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    Nmatrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg1)
        else:
            row_len = len(matrix[0])
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError('division by zero')
        if isinstance(row, list):
            a = 1
            for i in row:
                if not isinstance(i, (int, float)):
                    raise TypeError(msg1)
                if row_len != len(row):
                    raise TypeError(msg2)
                try:
                    Nmatrix1 = [round(ls1 / div, 2) for ls1 in row]
                    a = 0
                except TypeError:
                    a = 1
                    break
            if a == 0:
                Nmatrix.append(Nmatrix1)
            else:
                raise TypeError(msg1)
        else:
            raise TypeError(msg1)
    return (Nmatrix)
