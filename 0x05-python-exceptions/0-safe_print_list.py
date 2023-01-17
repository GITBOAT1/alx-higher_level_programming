#!/usr/bin/python3
''' Function that prints x elements of a list.'''


def safe_print_list(my_list=[], x=0):
    cur = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            cur = cur + 1
        except IndexError:
            print("")
            return (cur)
    if cur == x:
        print("")
    return (cur)
