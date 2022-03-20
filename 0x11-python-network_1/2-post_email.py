#!/usr/bin/python3
""" POST an email #0 """
from urllib import request, parse
import sys


def xhead(url, mail):
    """get the header X-Request-ID"""
    values = {'email': mail}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    with request.urlopen(url, data) as response:
        html = response.read().decode('utf-8')
        print(html)


if __name__ == "__main__":
    xhead(sys.argv[1], sys.argv[2])
