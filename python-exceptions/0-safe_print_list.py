#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if my_list and x > 0:
            pos = 0
            str_dev = ""
            for i in my_list:
                str_dev += str(i)
                pos += 1
                if pos == x:
                    break
        else:
            print("")
            return 0
    except TypeError:
        return pos
    else:
        print(str_dev)
        return pos
