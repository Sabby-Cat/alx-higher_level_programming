#!/usr/bin/python3
"""Python script fetches https://alx-intranet.hbtn.io/status"""

import requests
url = 'https://alx-intranet.hbtn.io/status'
with requests.get(url) as response:
    body = response.text
print('Body response:')
print(f'\t- type: {type(body)}')
print(f'\t- content: {body}')
