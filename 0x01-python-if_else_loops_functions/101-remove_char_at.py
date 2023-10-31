#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    nr = 0
    ret = ""
    for element in str:
        if nr == n:
            nr += 1
            continue
        ret += str[nr]
        nr += 1
    return ret
