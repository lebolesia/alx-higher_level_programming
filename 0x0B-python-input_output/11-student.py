#!/usr/bin/python3
"""Describes class student."""


class Student:
    """Symbolises student."""

    def __init__(self, first_name, last_name, age):
        """Activate new student.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtain dictionary symbol of student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Restore every attribute of student.

        Args:
            json (dict): Value pairs to restore attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
