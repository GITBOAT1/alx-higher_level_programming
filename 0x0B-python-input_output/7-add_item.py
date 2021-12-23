#!/usr/bin/python3
"""
Load, add, save
"""
import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

num = len(sys.argv)


try:
    data = load_from_json_file('add_item.json')
except Exception as a:
    data = []

for i in range(1, num):
    data.append(sys.argv[i])
save_to_json_file(data, 'add_item.json')
