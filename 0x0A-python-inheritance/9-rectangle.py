#!/usr/bin/python3
"""Describes class Rectangle that originates from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Symbolizes rectangle applying BaseGeometry."""

    def __init__(self, width, height):
        """Activate new Rectangle.

        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Replaces area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Replaces print() and str() symbol of Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
