#!/usr/bin/python3
"""

Divide a matrix

"""


def matrix_divided(matrix, div):
    """ this  this function divide """
    Nmatrix = []
    if len(matrix[0]) > len(matrix[1]):
       raise TypeError("Each row of the matrix must have the same size")
    if len(matrix) > 2:
        #raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    for i in range(matrix):
        test = []
        for a in range(i):
            if isinstance(a, (int, float)):
                test.append(a / div)
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        Nmatrix.append(test)
        del test
