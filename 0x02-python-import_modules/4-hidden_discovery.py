#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    elements = dir(hidden_4)

    for name in elements:
        if name[:1] != "_":
            print(name)
