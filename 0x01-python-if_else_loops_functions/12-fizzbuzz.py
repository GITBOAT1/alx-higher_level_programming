#!/usr/bin/python3
""" a function that prints the numbers from 1 to 100 separated by a space """


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print('Fizz', end=" ")
        elif i % 5 == 0:
            print('Buzz', end=" ")
        else:
            print('{}'.format(i), end=" ")
