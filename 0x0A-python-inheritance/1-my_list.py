#!/usr/bin/python3
""" Write a class MyList that inherits from list"""


class MyList(list):
    """class for MyList"""
    def print_sorted(self):
        print(sorted(self))
