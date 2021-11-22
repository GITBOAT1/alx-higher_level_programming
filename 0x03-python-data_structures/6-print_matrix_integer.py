#!/usr/bin/python3
"""Lists of lists
"""


def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        lt = matrix[i]
        for a in range(len(lt)):
            print("{:d} ".format(lt[a]), end="")
            if (a + 2) == len(lt):
                print("{:d}".format(lt[a + 1]))
                break
