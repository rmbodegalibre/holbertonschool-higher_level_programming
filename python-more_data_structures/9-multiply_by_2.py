#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    # print(new_dict)
    for key, value in a_dictionary.items():
        # print(value * 2)
        nval = value * 2
        # print(nval)
        new_dict[key] = nval
    return new_dict
