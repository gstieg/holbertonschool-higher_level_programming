#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for new_keys in sorted(a_dictionary):
        print("{}: {}".format(new_keys, a_dictionary[new_keys]))
