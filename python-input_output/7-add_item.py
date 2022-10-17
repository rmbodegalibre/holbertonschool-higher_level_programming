#!/usr/bin/python3
"""
This module contains a script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import os.path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if os.path.isfile(filename):
    """
    os.path.is - check if the path is an existing file
    """
    file_o = load_from_json_file(filename)
else:
    file_o = []
file_o.extend(sys.argv[1:])
"""
file_o.extend - get extension form file_object
"""
save_to_json_file(file_o, filename)
