#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ptr_to_func = fct(*args)
    except Exception as err:
        ptr_to_func = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return ptr_to_func
