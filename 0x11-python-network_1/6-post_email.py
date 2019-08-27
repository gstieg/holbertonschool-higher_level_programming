#!/usr/bin/python3
"""POST an email #1"""
import requests
from sys import argv

if __name__ == "__main__":
    print(requests.post(argv[1], {"email": argv[2]}).text)
