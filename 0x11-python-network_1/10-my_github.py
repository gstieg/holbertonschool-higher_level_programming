#!/usr/bin/python3
"""takes your Github credentials (username and password) and uses the Github
API to display your id"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        new = requests.get("https://api.github.com/user",
                           auth=(argv[1], argv[2]))
        print(new.json.get('id'))
    except:
        print("None")
