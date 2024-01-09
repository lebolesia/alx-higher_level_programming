#!/usr/bin/python3
"""Describes file-writing funct."""


def write_file(filename="", text=""):
    """Write stri to UTF8 text file.

    Args:
        filename (str): Name of file to write.
        text (str): Text to write to file.
    Returns:
        The numb of chara written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
