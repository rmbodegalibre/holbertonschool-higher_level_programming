#!/usr/bin/python3

def element_at(my_list, idx):

    qtty = len(my_list)
    if idx <= qtty:
        elem = my_list[idx]
        return elem if idx >= 0 else None
    else:
        return None
