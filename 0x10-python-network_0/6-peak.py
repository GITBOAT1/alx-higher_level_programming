#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ a function that finds a peak in a list of unsorted integers """

    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return(list_of_integers[len(list_of_integers)-1])
    else:
        return


if __name__ == __name__:
    find_peak
