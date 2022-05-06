#!/usr/bin/python3
"""
This script is used to create a basic calculator in python.

Author: Ricardo Montaña
Date: 5-05-2022
"""

if __name__ == "__main__":
    
    from calculator_1 import *
    import sys
    num_args = len(sys.argv) - 1
    #print(num_args)
    #print(sys.argv[0])
    #print(sys.argv[1])
    #print(sys.argv[2])
    #print(sys.argv[3])
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if op not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif op == "+":
            print(f"{a} + {b} = {add(a, b)}")
        elif op == "-":
            print(f"{a} - {b} = {sub(a, b)}")
        elif op == "*":
            print(f"{a} * {b} = {mul(a, b)}")
        else:
            print(f"{a} / {b} = {div(a, b)}")
