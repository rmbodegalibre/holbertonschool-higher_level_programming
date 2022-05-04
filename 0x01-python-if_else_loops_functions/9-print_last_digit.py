#!/usr/bin/python3

def print_last_digit(number):
    lastd = abs(number) % 10
    print(f"{lastd}", end="")
    return lastd
