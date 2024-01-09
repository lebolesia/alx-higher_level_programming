#!/usr/bin/python3
# 6-from_json_string.py
"""Describes JSON-to-object funct."""
import json


def from_json_string(my_str):
    """Replaces Python object symbol of JSON stri."""
    return json.loads(my_str)
