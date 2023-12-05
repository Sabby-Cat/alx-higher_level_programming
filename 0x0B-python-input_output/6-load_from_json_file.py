#!/usr/bin/python3
"""obj from json file"""
import json


def load_from_json_file(filename):
    """creates file from json"""
    with open(filename, 'r', encoding="utf-8") as file:
        json.load(file)
