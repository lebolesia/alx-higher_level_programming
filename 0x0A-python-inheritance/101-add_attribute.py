#!/usr/bin/python3
"""Describes funct that attaches characters to objects."""


def add_attribute(obj, att, value):
    """Attaches new character to object if achievable.

    Args:
        obj (any): Object to attach character to.
        att (str): Name of character to attach to object.
        value (any): Value of character.
    Raises:
        TypeError: If character cannot be attached.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
