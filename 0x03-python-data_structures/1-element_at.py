#!/usr/bin/python3

def element_at(my_list, idx):

    elem = my_list[idx]
    qtty = len(my_list)

    return elem if (0 <= idx < qtty) else None 
