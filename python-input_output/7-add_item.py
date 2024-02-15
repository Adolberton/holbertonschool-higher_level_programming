#!/usr/bin/python3
"""holberton mandatory doc"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item(args):
    """holberton mandatory doc"""
    filename = "add_item.json"
    list = []
    for _ in args[1:]:
        list += _
    save_to_json_file(list, filename)
