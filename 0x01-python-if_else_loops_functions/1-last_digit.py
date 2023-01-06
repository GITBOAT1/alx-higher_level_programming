#!/usr/bin/python3
""" Program to check if  last digit is >5 or <5 or == 0 """
import random
number = random.randint(-10000, 10000)

s = "Last digit of"
strn = "and is less than 6 and not 0"
la = number % 10
""" check if its nagative """
if (number < 0):
    la = int(str(number)[-1:])
    la = (-1) * la
    print("{} {:d} is {:d} and is less than 6 and not 0".format(s, number, la))
else:
    if int(la) > 5:
        print("{} {:d} is {:d} and is greater than 5".format(s, number, la))
    elif int(la) == 0:
        print("{} {:d} is {:d} and is 0".format(s, number, la))
    elif int(la) < 6 and int(la) != 0:
        print("{} {:d} is {:d} {}".format(s, number, la, strn))
