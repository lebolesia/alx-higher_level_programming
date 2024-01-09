#!/usr/bin/python3
"""Describes file-attaching funct."""


def append_write(filename="", text=""):
    """Attaches stri to end of UTF8 text file.

    Args:
        filename (str): Name of file to attach to.
        text (str): Stri to attach to file.
    Returns:
        Numb of chara attached.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
