#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the variable "X-Request-Id" in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(dict(r.headers).get('X-Request-Id'))
