#!/usr/bin/python3
for i in range(90):
    div = i / 10
    mod = i % 10

    if mod > div:
        if i != 89:
            print('{:02d}'.format(i), end=", ")
        else:
            print('{:02d}'.format(i))
