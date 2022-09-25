#!/usr/bin/python3
"""
This script akes in a letter and sends a POST request to
"http://0.0.0.0:5000/search_user" with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data)

    print(dir(req))
