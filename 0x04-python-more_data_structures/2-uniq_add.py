#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    tot = 0
    for i in new:
        tot += i
    return tot
