#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    script_name = sys.argv[0]
    num_args = len(sys.argv) - 1
    args_names = str(sys.argv)

    if __name__ == "__main__":
        if num_args == 0:
            print("0 arguments.")
        elif num_args == 1:
            print("1 argument:")
        else:
            print(f"{num_args} arguments:")
        for lst in range(num_args):
            print(f"{lst + 1}: {sys.argv[lst + 1]}")
