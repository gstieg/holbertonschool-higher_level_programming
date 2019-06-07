#!/usr/bin/python3
import json
"""importing json"""


def from_json_string(my_str):
    """ args:
    my_str: the string
    """
    return json.loads(my_str)
