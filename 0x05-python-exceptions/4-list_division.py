#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    retl = []
    for i in range(list_length):
        ans = 0
        try:
            ans = my_list_1[i] / my_list_2[i]
        except:

