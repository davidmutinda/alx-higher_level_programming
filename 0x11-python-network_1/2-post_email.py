#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = urllib.parse.urlencode(argv[2])
    email = email.encode()
    req = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(req) as response:
        print(response.read())

