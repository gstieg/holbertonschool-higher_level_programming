#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>
"""

def say_my_name(first_name, last_name=""):
    """
    prints first and last name given
    """

    if type(first_name) is not str:
        raise TypeError("first_namee must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))