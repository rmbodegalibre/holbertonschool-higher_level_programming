#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)
    else:
        lit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        itg = 0
        for idx in range(len(roman_string)):
            if idx > 0 and lit[roman_string[idx]] > lit[roman_string[idx - 1]]:
                itg += lit[roman_string[idx]] -2 * lit[roman_string[idx - 1]]
            else:
                itg += lit[roman_string[idx]]
        return itg
