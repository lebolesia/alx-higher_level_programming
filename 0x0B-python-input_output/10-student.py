#!/usr/bin/python3
"""Describes class student."""


class Student:
    """Symbolise student."""

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
        """Obtain dictionary symbol of the student.

        If characteritsic is list of stri, symbolises just those characteristics
        comprised in list.

        Args:
            attrs (list): (Optional) Characteristics to symbolise.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
