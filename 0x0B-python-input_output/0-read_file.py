#!/usr/bin/python3
def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""

    """ args:
    filename: name of the file
    """
    with open(filename, encoding='utf-8') as file1:
        print(file1.read())
