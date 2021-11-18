#!/bin/python3
def Lcase():
    for i in range(97, 123):
        if ((i == (97+4)) or (i == (97+16))):
            pass
        else:
            print(chr(i), end="")

            
Lcase()
