#!/usr/bin/python3
import json
"""importing json"""


def save_to_json_file(my_obj, filename):
    """ args:
    my_obj: object
    filename: the name of the file
    """
    with open(filename, 'a', encoding='utf-8') as a:
        json.dump(my_obj, a)
