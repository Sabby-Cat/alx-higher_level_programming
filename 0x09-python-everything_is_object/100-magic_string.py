#!/usr/bin/python3
def magic_string():
    magic_string.nr = getattr(magic_string, 'nr', 0) + 1
    return "BestSchool, " * (magic_string.nr - 1) + "BestSchool"
