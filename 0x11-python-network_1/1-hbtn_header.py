#!/usr/bin/python3
from urllib import request
import sys
""" display the header """


def xhead(x):
    """get the header X-Request-ID"""
    with request.urlopen(x) as resp:
        data = resp.getheader('X-Request-ID')
        print(data)


if __name__ == __name__:
    if sys.argv[1]:
        xhead(sys.argv[1])
