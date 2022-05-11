#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list2 = my_list
    for idx, value in enumerate(list2):
        if value == search:
            list2[idx] = replace
    return list2
