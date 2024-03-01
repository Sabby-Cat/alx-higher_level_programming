#!/usr/bin/python3
"""Python script send request to URL and display
value of var in response header"""
import requests
import sys


if __name__ == '__main__':
    bodyRes = requests.get(sys.argv[1])
    print(bodyRes.headers.get('X-Request-Id'))
