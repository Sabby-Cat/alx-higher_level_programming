#!/usr/bin/python3
"""Python script take in URL and email adres,
send POST request to passed URL with email,
and displays body of response"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
