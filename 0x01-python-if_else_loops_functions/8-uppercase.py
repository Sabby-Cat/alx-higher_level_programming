#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if i > 96 and i < 123:
            i -= 32
        i = chr(i)
        print("{}".format(i), end='')
    print()
