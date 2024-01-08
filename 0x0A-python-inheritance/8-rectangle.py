#!/usr/bin/python3
"""Describes class Rectangle that originates from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Symbolize rectangle applying BaseGeometry."""

    def __init__(self, width, height):
        """Activate new Rectangle.

        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
