#!/usr/bin/python3
"""holberton mandatory doc"""


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

list = load_from_json_file(filename)
list.extend(sys.argv[1:])
save_to_json_file(list, filename)
