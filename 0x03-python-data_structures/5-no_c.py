#!/usr/bin/python3

def no_c(my_string):

    lng = len(my_string)
    new_string = ""

    for idx in range(0, lng):
        if my_string[idx] == 'c' or my_string[idx] == 'C':
            new_string = new_string + ""
        else:
            new_string = new_string + my_string[idx]
    return (new_string)
