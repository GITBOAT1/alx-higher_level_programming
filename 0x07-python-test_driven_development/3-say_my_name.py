#!/usr/bin/python3
"""

 a function that prints My name is <first name> <last name>

"""

msg1 = "first_name must be a string"
msg2 = "last_name must be a string"


def say_my_name(first_name, last_name=""):
    """ a function that prints My name is <first name> <last name> """
    if not isinstance(first_name, str):
        raise TypeError(msg1)
    if not isinstance(last_name, str):
        raise TypeError(msg2)
    else:
        print("My name is {} {}".format(first_name, last_name))
