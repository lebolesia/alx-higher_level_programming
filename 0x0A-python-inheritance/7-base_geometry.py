#!/usr/bin/python3
"""Describes base geometry class BaseGeometry."""


class BaseGeometry:
    """Symbolizes base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Confirm paramet as integer.

        Args:
            name (str): Name of paramet.
            value (int): Paramet to confirm.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
