#!/usr/bin/python3
"""Describes string-to-JSON funct."""
import json


def to_json_string(my_obj):
    """Replaces JSON symbol of stri object."""
    return json.dumps(my_obj)
