#!/usr/bin/python3
for i in range(97, 123):
    if ((i == (97+4)) or (i == (97+16))):
        pass
    else:
        print('{}'.format(chr(i)), end="")
