#!/usr/bin/python3
""" Doc """

add_integer = __import__('0-add_integer').add_integer

try:
    print(add_integer(1, "2"))
except Exception as e:
    print(e)
