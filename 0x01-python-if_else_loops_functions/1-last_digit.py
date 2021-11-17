#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = int(str(number)[-1:])
s = "Last digit of"
if int(l) > 5:
    print("{} {:d} is {:d} and is greater than 5".format(s, number, l))
elif int(l) == 0:
    print("{} {:d} is {:d} and is 0".format(s, number, l))
elif int(l) < 6 and int(l) > 0 :
    print("{} {:d} is {:d} and is less than 6 and not 0".format(s, number, l))
