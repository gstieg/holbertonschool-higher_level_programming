#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict(a_dictionary)
    for value in a_dictionary:
            new_dictionary[value] *= 2
    return new_dictionary
