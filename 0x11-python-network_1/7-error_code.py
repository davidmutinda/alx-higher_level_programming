#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print(f'Error code: {req.status_code}')
    else:
        print(req.text)
