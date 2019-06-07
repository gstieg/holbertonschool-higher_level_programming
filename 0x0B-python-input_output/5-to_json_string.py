#!/usr/bin/python3
import json
"""importing json"""


def to_json_string(my_obj):
    """JSON representation of an object (string):
    args:
    my_obj: the object being returned
    """
    return json.dumps(my_obj)
