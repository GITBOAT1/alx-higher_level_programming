#!/usr/bin/python3
''' A function that checks for lowercase character '''


def uppercase(str):
    strupper = ""
    for i in str:
        if ord(i) >= 97:
            strupper += chr(ord(i) - 32)
        else:
            strupper += i
    print('{}'.format(strupper))
