#!/usr/bin/python3
"""text files insert function"""


def append_after(filename="", search_string="", new_string=""):
    """appends after specific text"""
    text = ""
    with open(filename) as rf:
        for line in rf:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wf:
        wf.write(text)
