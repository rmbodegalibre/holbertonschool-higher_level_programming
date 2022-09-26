#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search not in my_list:
        return my_list
    else:
        new_list = list(my_list)
        it = 0
        for i in new_list:
            if i == search:
                new_list[it] = replace
            it += 1
        return new_list
