#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""

def text_indentation(text):
    """
    indention
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n"
