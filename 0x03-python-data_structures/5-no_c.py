#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for num in my_string:
        if num != "c" and num != "C":
            new_str += num
    return new_str
