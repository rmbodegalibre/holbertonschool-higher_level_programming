#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
#my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    qtty = 0
    elem = 0
    #x = 5

    try:
        while elem < x:
            if isinstance(my_list[elem], int):
                qtty += 1
                print("{:d}".format(my_list[elem]), end="")
            elem += 1
    except TypeError as err:
        print(err)
    else:
        print("")
        # print("nb_print: {:d}".format(qtty))
        return qtty
