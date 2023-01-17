#!/usr/bin/python3
''' Write a function that divides element by element 2 lists. '''


def list_division(my_list_1, my_list_2, list_length):
    cur = 0
    result = []
    for i in range(list_length):
        try:
            divi = my_list_1[i] / my_list_2[i]
            result.append(divi)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
