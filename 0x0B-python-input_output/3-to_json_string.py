#!/usr/bin/python3
"""
To JSON epresentation of an object

"""
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string):
    Args
       my_obj

    """
    return(json.dumps(my_obj))
