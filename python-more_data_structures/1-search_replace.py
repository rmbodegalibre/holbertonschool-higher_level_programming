#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ind = my_list.index(search)
    new_list = list(my_list)
    new_list[ind] = replace
    return new_list
