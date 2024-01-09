#!/usr/bin/python3
"""Describes text file-reading funct."""


def read_file(filename=""):
    """Print details of UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
