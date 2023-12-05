#!/usr/bin/python3
"""turns json to obj"""
import json


def from_json_string(my_str):
    """makes json file into object"""
    return json.loads(my_str)
