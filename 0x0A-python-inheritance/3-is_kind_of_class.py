#!/usr/bin/python3
"""Describes class as well as origonal class-checking funct."""


def is_kind_of_class(obj, a_class):
    """Test whether object is an example or original example of a class.

    Args:
        obj (any): Object to test.
        a_class (type): Class togo with kind of object to.
    Returns:
        If object is an example or original example of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
