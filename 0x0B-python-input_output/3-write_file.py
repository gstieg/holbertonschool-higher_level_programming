#!/usr/bin/python3
"""write a string to a  file"""


def write_file(filename="", text=""):
    """ args:
    filename: name of the files
    text: text for the sting in file
    """
    with open(filename, 'w', encoding='utf-8') as a:
        return a.write(text)
