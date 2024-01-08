#!/usr/bin/python3
"""Describes original class-checking funct."""


def inherits_from(obj, a_class):
    """Tests whether object is original example of class.

    Args:
        obj (any): Object to test.
        a_class (type): Class to go with kind of object to.
    Returns:
        If object is original example of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
