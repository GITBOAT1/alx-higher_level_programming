#!/usr/bin/python3
''' a function that creates a copy of the string,
    removing the character at the position n
    (not the Python way, the “C array index”).
'''


def remove_char_at(str, n):
    str1 = ""
    for i in range(len(str)):
        if i != n:
            str1 += str[i]
    return str1
