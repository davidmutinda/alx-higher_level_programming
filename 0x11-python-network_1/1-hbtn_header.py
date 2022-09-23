#!/usr/bin/python3
"""
This script akes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
from sys import argv
import urllib.request

req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    print(dict(response.headers)['X-Request-Id'])
