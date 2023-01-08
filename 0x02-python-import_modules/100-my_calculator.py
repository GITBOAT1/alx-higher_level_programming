#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def msg():
    """ print error msg """

    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)


def cal(a, b, c):
    """ rogram that imports all functions from the file calculator_1.py """

    a = int(a)
    c = int(c)
    oprator = ['+', '-', '*', '/']
    if b not in oprator:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        ans = 0
        if b == '+':
            ans = add(a, c)
        elif b == '-':
            ans = sub(a, c)
        elif b == '*':
            ans = mul(a, c)
        elif b == '/':
            ans = div(a, c)
        print('{} {} {} = {}'.format(a, b, c, ans))


if __name__ == "__main__":
    if len(sys.argv) == 4:
        cal(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        msg()
