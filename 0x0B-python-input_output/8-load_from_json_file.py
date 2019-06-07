#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ args:
    filename: the name of the file
    """
    with open(filename) as a:
        return json.load(a)
