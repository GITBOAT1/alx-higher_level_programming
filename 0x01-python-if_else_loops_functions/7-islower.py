#!/usr/bin/python3
''' A function that checks for lowercase character '''


def islower(c):
    a = ord(c)
    if int(a) >= 97 and int(a) <= 122:
        return True
    elif int(a) >= 65 and int(a) <= 90:
        return False
