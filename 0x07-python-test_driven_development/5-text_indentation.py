#!/usr/bin/python3
"""

 a function that prints My name is <first name> <last name>

"""

msg1 = "text must be a string"


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError(msg1)
    else:
        for i in text:
            if i == '.' or i == '?' or i == ':':
                print("\n")
            else:
                print(i, end="")
