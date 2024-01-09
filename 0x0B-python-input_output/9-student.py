#!/usr/bin/python3
"""Describes class pupil."""


class Student:
    """Symbolise pupil."""

    def __init__(self, first_name, last_name, age):
        """Activate new pupil.

        Args:
            first_name (str): First name of pupil.
            last_name (str): Last name of pupil.
            age (int): Age of pupil.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obtain dictionary symbol of pupil."""
        return self.__dict__
