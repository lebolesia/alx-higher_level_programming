#!/usr/bin/python3
"""Desbribes Rectan class."""


class Rectangle:
    """Symbolizes rectangle."""

    def __init__(self, width=0, height=0):
        """Activate new Rectangle.

        Args:
            width (int): Width of new rectang
            height (int): Height of new rectang
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Place width of rectang."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width has to be integer")
        if value < 0:
            raise ValueError("width has to be >= 0")
        self.__width = value

    @property
    def height(self):
        """Place height of rectang."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height has to be integer")
        if value < 0:
            raise ValueError("height has to be >= 0")
        self.__height = value
