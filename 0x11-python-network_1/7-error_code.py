#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
from sys import argv
import requests


if __name__ == "__main__":
    try:
        req = requests.get(argv[1], auth=('user', 'pass'))
        print(req.read().decode('utf-8'))
    except Exception as e:
        print('Error code:', e.code)
