#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-I"""
import requests
import sys


if __name__ == "__main__":
    new = requests.get(sys.argv[1])
    print(new.headers.get('X-Request-Id'))
