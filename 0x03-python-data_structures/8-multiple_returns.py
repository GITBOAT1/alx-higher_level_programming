#!/usr/bin/python3
"""More on returns
"""


def multiple_returns(sentence):
    lo = []
    se = len(sentence)
    if se <= 0:
        lo = [se, None]
        return (tuple(lo))
    else:
        lo = [se, sentence[0]]
        return (tuple(lo))
