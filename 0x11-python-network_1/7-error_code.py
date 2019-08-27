#!/usr/bin/python3
"""comment"""
import requests
from sys import argv

if __name__ == "__main__":
    new = requests.get(argv[1])
    if new.status_code <= 400:
        print(new.text)
    else:
        print("Error code: {}".format(new.status_code))
