#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ agrs:
    filename = name of the file"""

    with open(filename, encoding='utf-8') as a:
        for line in a:
            print(line, end="")
