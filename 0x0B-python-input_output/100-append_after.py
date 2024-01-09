#!/usr/bin/python3
"""Describes text file insertion funct."""


def append_after(filename="", search_string="", new_string=""):
    """Add text after every line consisting of particular stri in file.

    Args:
        filename (str): Name of file.
        search_string (str): Stri to search for in file.
        new_string (str): Stri to add.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
