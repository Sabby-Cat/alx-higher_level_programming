#!/usr/bin/python3
import calculator_1
from sys import argv, exit
if __name__ == "__main__":
    nr = len(argv) - 1
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sin = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(sin.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, sin[argv[2]](a, b)))
