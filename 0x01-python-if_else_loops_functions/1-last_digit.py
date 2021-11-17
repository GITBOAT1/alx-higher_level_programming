#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
la = int(str(number)[-1:])
s = "Last digit of"
if int(la) > 5:
    print("{} {:d} is {:d} and is greater than 5".format(s, number, la))
elif int(la) == 0:
    print("{} {:d} is {:d} and is 0".format(s, number, la))
elif int(la) < 6 and int(la) != 0:
    if number < 0:
        la = -1 * la
    print("{} {:d} is {:d} and is less than 6 and not 0".format(s, number, la))
