#!/usr/bin/python3
""" display the header """
from urllib import request
import sys



def xhead(x):
    """get the header X-Request-ID"""
    with request.urlopen(x) as resp:
        data = resp.getheader('X-Request-ID')
        print(data)


if __name__ == "__main__":
    xhead(sys.argv[1])
