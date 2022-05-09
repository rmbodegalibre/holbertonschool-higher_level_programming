#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    qtty = len(my_list)

    if (0 <= idx < qtty):
        my_list[idx] = element
    return my_list
