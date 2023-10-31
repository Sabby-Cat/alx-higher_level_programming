#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    ret = ""
    for i in str:
        if i == n:
            i += 1
            continue
        ret += str[i]
    return ret
