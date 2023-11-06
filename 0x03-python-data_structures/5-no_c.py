#!/usr/bin/python3
def no_c(my_string):
    dict = {67: 0, 99: 0}
    new = my_string.translate(dict)
    return new
