#!/usr/bin/python3
"""Describes original list class MyList."""


class MyList(list):
    """Applies arranged printing for fixed list class."""

    def print_sorted(self):
        """Print list in arranged ascending order."""
        print(sorted(self))
