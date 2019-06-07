#!/usr/bin/python3
import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    a  = load_from_json_file("add_item.json")
    save_to_json_file(a + sys.argv[1:], "add_item.json")
except:
    save_to_json_file(sys.argv[1:], "add_item.json")
