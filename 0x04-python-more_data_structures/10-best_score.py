#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    if not a_dictionary.values:
        return None
    return max(a_dictionary)
