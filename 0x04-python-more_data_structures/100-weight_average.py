#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sco = 0
    wei = 0
    for x in my_list:
        sco += x[0] * x[1]
        wei += x[1]
    return (sco / wei)
