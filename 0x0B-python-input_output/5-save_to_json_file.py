#!/usr/bin/python3
"""Describes JSON file-writing funct."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file applying JSON symbol."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
