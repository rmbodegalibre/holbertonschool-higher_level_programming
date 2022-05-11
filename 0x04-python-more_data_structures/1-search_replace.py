#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list2 = []
    for idx, value in enumerate(my_list):
        if value == search:
            list2.append(replace)
        else:
            list2.append(my_list[idx])
    return list2
