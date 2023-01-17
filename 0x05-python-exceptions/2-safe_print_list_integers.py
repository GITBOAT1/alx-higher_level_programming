#!/usr/bin/python3
''' unction that prints the first x elements of a list and only integers'''


def safe_print_list_integers(my_list=[], x=0):
    cur = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            cur = cur + 1
        except (TypeError, ValueError):
            pass
    print("")
    return cur
