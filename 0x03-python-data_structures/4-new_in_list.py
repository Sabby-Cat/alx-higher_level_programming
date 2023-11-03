#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    dup = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        dup[idx] = element
        return dup
    else:
        return dup
