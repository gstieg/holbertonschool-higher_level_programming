#!/usr/bin/python3
def append_write(filename="", text=""):
    """ args:
    filename: name of the file
    text: text
    """
    with open(filename, 'a', encoding='utf-8') as a:
        return a.write(text)
