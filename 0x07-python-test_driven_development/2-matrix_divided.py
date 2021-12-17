#!/usr/bin/python3
"""

Divide a matrix

"""


def matrix_divided(matrix, div):
    """ this  this function divide """
    j = "matrix must be a matrix (list of lists) of integers/float"
    Nmatrix = []
    try:
        if len(matrix) != 2:
            raise TypeError("Each row of the matrix must have the same size")
        elif len(matrix[0]) != len(matrix[1]):
            raise TypeError("matrix must have each row with the same size")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        elif not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        else:
            for i in matrix:
                test = []
                for a in i:
                    if isinstance(a, (int, float)):
                        t = round(a / div, 2)
                        test.append(t)
                    else:
                        raise TypeError(j)
                Nmatrix.append(test)
                del test
            return(Nmatrix)
    except Exception as e:
        print(e)
