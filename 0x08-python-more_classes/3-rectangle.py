#!/usr/bin/python3
"""Describes rectang class."""


class Rectangle:
    """Symbolizes rectang."""

    def __init__(self, width=0, height=0):
        """Activate new rectang.

        Args:
            width (int): Width of new rectang.
            height (int): Height of new rectang.
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

    def area(self):
        """Return area of rectang."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimet of rectang."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Replace printable copy of rectang.

        Symbolizes rectang with # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
