#!/usr/bin/python3
"""Describes JSON file-reading funct."""
import json


def load_from_json_file(filename):
    """Forms Python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
