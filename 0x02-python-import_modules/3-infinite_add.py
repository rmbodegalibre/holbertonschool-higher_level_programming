#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    script_name = sys.argv[0]
    num_args = len(sys.argv) - 1
    sm = 0

    for nums in range(num_args):
        sm = sm + int(sys.argv[nums + 1]) 
    print(f"{sm}")
