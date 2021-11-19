#!/usr/bin/python3
"""Searching for hidden file"""
import hidden_4
import types

if __name__ == '__main__':
    doc = dir(hidden_4)
    for i in range(len(doc)):
        a = doc[i]
        if (a[0] != ("_")):
            print(doc[i])
