#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nr = len(argv) - 1
    if nr == 0:
        print("0 arguments.")
    elif nr == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nr))
    for i in range(nr):
        print("{}: {}".format(i + 1, argv[i + 1]))
