#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        #if isinstance(dvdo, int) and isinstance(dvsr, int):
        try:
            new_coc = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            new_coc = 0
        except TypeError:
            print("wrong type")
            new_coc = 0
        except IndexError:
            print("out of range")
            new_coc = 0
        finally:
            new_list.append(new_coc)
    return new_list
