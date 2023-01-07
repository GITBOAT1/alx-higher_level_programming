#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        lo = chr(ord('z') - i)
        print('{}'.format(lo), end="")
    else:
        up = chr(ord('Z') - i)
        print('{}'.format(up), end="")
