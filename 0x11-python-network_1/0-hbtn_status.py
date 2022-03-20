#!/usr/bin/python3
from urllib import request
""" display the status """


def stats():
    """get the status of alx-intra"""
    html = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(html) as resp:
        data = resp.read()
        decode = data.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(decode))


if __name__ == __name__:
    stats()
