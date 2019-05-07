#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx >= 0 or idx < len(new_list):
        for num in my_list:
            new_list.append(num)
        new_list[idx] = element
        return new_list
    else:
            return my_list
