#!/usr/bin/python3
"""Describes class-checking funct."""


def is_same_class(obj, a_class):
    """Test whether object is precisely an example of particular class.

    Args:
        obj (any): Object to test.
        a_class (type): Class to go with type of object to.
    Returns:
        If object is precisely an example of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
