#!/usr/bin/python3
"""
this  adds 2 integers.
"""

def add_integer(a, b=98):
    """
    a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) and type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
