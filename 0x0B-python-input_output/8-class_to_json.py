#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Replace dictionary symbol of basic data struct."""
    return obj.__dict__
