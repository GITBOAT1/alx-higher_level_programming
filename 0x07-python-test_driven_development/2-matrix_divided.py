#!/usr/bin/python3
"""

Divide a matrix

"""


def matrix_divided(matrix, div):
    """ this  this function divide """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "matrix must have each row with the same size"
    Nmatrix = []

    for row in matrix:
        row_len = len(matrix[0])
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError('division by zero')
        if isinstance(row, list):
            for i in row:
                if not isinstance(i, (int, float)):
                    raise TypeError(msg1)
                if row_len != len(row):
                    raise TypeError(msg2)
                Nmatrix1 = [round(ls1 / div, 2) for ls1 in row]
            Nmatrix.append(Nmatrix1)
        else:
            raise TypeError(msg1)
    return (Nmatrix)
