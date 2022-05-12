#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)
    else:
        letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        integer = 0
        for idx in range(len(roman_string)):
            if idx > 0 and letters[roman_string[idx]] > letters[roman_string[idx - 1]]:
                integer += letters[roman_string[idx]] -2 * letters[roman_string[idx - 1]]
            else:
                integer += letters[roman_string[idx]]
        return integer
