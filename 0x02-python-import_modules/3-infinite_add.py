#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    tot = 0
    for i in range(len(argv) - 1):
        tot += int(argv[i + 1])
    print("{}".format(tot))
